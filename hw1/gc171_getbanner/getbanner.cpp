#include <iostream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <cstring>
#include <netdb.h>

using namespace std;

int hostname_to_ip(char *, char *);

int main(int argc, char *argv[])
{
    if (argc < 3)
    {
        cout << "Usage: ./getbanner <host> <port>" << endl;
        return EXIT_FAILURE;
    }

    // domain to ip
    char *ip;
    if (hostname_to_ip(argv[1], ip) == EXIT_FAILURE)
    {
        cout << "no such domain/ip" << endl;
    }

    struct sockaddr_in host_addr;
    host_addr.sin_family = AF_INET;
    host_addr.sin_addr.s_addr = inet_addr(ip);
    host_addr.sin_port = htons(atoi(argv[2]));

    int sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0)
    {
        cout << "err creating socket" << endl;
        return EXIT_FAILURE;
    }

    if (connect(sockfd, (struct sockaddr *)&host_addr, sizeof(host_addr)) < 0)
    {
        cout << "err connect server" << endl;
        return EXIT_FAILURE;
    }

    char msg[] = "QUIT\n";
    send(sockfd, msg, strlen(msg), 0);

    char data_buffer[1024];
    memset(data_buffer, '0', sizeof(data_buffer));

    int rd = 0;
    while ((rd = read(sockfd, data_buffer, sizeof(data_buffer) - 1)) > 0)
    {
        data_buffer[rd] = 0;
        if (fputs(data_buffer, stdout) == EOF)
        {
            cout << "\nStandard output error" << endl;
        }
    }
    close(sockfd);

    return EXIT_SUCCESS;
}
/**
 * convert domain to ip
 */

int hostname_to_ip(char *hostname, char *ip)
{
    struct hostent *he;
    struct in_addr **addr_list;
    int i;

    he = gethostbyname(hostname);
    if (he == NULL)
    {
        // get the host info
        herror("gethostbyname");
        return EXIT_FAILURE;
    }

    addr_list = (struct in_addr **)he->h_addr_list;

    for (i = 0; addr_list[i] != NULL; i++)
    {
        //Return the first one;
        strcpy(ip, inet_ntoa(*addr_list[i]));
        return EXIT_SUCCESS;
    }

    return EXIT_FAILURE;
}