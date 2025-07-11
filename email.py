import streamlit as st
import smtplib

def send_email():
    st.title("📧 Gmail Email Sender")

    st.markdown("**Note:** You must use an [App Password](https://support.google.com/accounts/answer/185833) instead of your Gmail password.")

    sender_email = st.text_input("✉️ Your Gmail Address")
    sender_password = st.text_input("🔑 App Password", type="password")
    receiver_email = st.text_input("📨 Receiver's Email Address")
    subject = st.text_input("📝 Subject")
    message_body = st.text_area("💬 Message")

    if st.button("📤 Send Email"):
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()  # Secure the connection
                server.login(sender_email, sender_password)
                
                message = f"Subject: {subject}\n\n{message_body}"
                server.sendmail(sender_email, receiver_email, message)
            
            st.success("✅ Email sent successfully!")
        except Exception as e:
            st.error(f"❌ Error: {e}")

# Run the function when script executes
if __name__ == "__main__":
    send_email()
