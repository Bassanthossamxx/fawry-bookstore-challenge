class MailService:
    def send(self, book_title, email, filetype):
        print(f"Book Store: Sending '{book_title}.{filetype}' to email: {email}")
