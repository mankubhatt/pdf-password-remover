import pikepdf

def remove_password_from_pdf(filename, password):
    pikepdf.settings.encryption_provider = 'cryptography'
    pdf = pikepdf.open(filename, password=password)
    pdf.save("/Users/mayankbhatt/Downloads/Mayank/Salary Slips/Dec-23.pdf")

def set_password_for_pdf(filename, password):
    pikepdf.settings.encryption_provider = 'cryptography'
    pdf = pikepdf.Pdf.open(filename)    
    pdf.save('/Users/mayankbhatt/Downloads/Pankaj-Sbi.pdf', encryption=pikepdf.Encryption(owner=password, user=password, R=6))

if __name__ == "__main__":
    file_path = "/Users/mayankbhatt/Downloads/Mayank/Salary Slips/Dec-23.pdf"
    password = input("Enter Your Pdf Password\n")
    remove_password_from_pdf(file_path, password)