import webbrowser
import pyautogui
import time

# 📌 Enter the phone number of the target (Include country code, e.g., +923XXXXXXXXX)
phone_number = "+923XXXXXXXXX"  # Change this to the number of your target

# 📌 Message to be sent
message = "This is a prank! 😂"

# 📌 Number of times to send the message
repeat_count = 50  # Adjust as needed

# 📌 Open WhatsApp Web with the target's chat
whatsapp_url = f"https://web.whatsapp.com/send?phone={phone_number}"
webbrowser.open(whatsapp_url)

print("🚀 Opening WhatsApp Web... Please wait 10 seconds.")
time.sleep(10)  # Wait for WhatsApp Web to load

# 📌 Sending messages in a loop
try:
    for i in range(repeat_count):
        pyautogui.write(message)  # Type the message
        pyautogui.press("enter")  # Send the message
        print(f"✅ Message {i+1} sent!")

        time.sleep(1 + (time.time() % 2))  # Random delay of 1-2 seconds

    print("🎉 All messages sent successfully!")

except Exception as e:
    print(f"❌ Error: {e}")
    print("Make sure WhatsApp Web is open and focused.")
