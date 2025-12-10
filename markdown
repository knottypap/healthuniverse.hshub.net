START

1. Initialize Order Form
   - Load form from internal domain only (berries.hshub.net/order or local server)
   - Disable external scripts, iframes, and remote includes
   - Require HTTPS + HSTS policy

2. Validate Page Origin
   IF window.location.hostname != "berries.hshub.net"
       THEN terminate process and redirect to safe internal page / error screen
       ELSE continue

3. Accept Customer Input
   - Name, Email, Address, Product Selection, Quantity
   - Validate fields client-side and server-side
   - Reject script tags, links, external URLs, redirects

4. Submit Order
   On submission:
        A) Send POST request ONLY to server at berries.hshub.net
        B) Reject any form action containing:
             http://, https://, ftp://, or domain not equal to berries.hshub.net
        C) Block execution if referer header OR origin is not internal domain

   IF request.origin != "berries.hshub.net"
       THEN deny submission + log security alert

5. Payment Processing
   - Use internal gateway or secure payment API wrapped server-side
   - Never expose checkout redirection URL to client
   - Process payment through back-end only:
        Customer → berries.hshub.net → Payment API (server side only)
        (No browser-visible external link)

6. Confirmation
   IF payment.status == success
        Display confirmation page on berries.hshub.net/confirmation
        Send email receipt
   ELSE
        Display error on internal page, offer retry (internal only)

7. Post-Order Protection
   - Sanitize database input
   - Track suspicious redirect attempts
   - Auto-block IP if redirect injection detected

END
