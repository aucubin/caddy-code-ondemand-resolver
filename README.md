# Caddy Code Ondemand Resolver

## Idea
When using code-server you can access ports on the machine via the <port>.<machine-name> endpoint.
As Caddy does not allow wildcard certificates to be created with the normal http challenge for an acme endpoint on-demand tls needs to be used in this scenario.
To make on-demand tls more secure a http api can be used that caddy then asks before requesting a certificate for a subdomain.
This Resolver just contains a basic http api that returns 200 OK if the subdomain is a port number and 403 Forbidden if it not.

Note: The API does not contain any authentication and should only be exposed directly internally on the machine where the caddy server is running.