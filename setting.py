from taipy import Gui
from taipy import Config
from taipy import Core
from taipy.gui import Markdown

page = """
<h3 class="h5">ManagMed</h3>
# Settings

## Personalize Your Experience

### Account Settings
- **Profile Information:** Update your personal details, ensuring accurate and relevant information.
- **Change Password:** Maintain the security of your account by updating your password regularly.

### Notifications
- **Medication Reminders:** Customize the frequency and timing of your medication reminders.
- **News and Updates:** Choose your preferences for receiving notifications about new medications, recalls, and announcements.

## App Preferences

### Theme
- **Choose Theme:** Select your preferred color scheme for a personalized app experience.
- **Dark Mode:** Enable or disable dark mode for comfortable usage, especially during nighttime.

### Language
- **App Language:** Set the language of the app interface to your preference for better understanding and usability.

## Privacy and Security

### Data Security
- **Biometric Authentication:** Enhance the security of your app with fingerprint or face recognition.
- **Logout:** Securely sign out from your account when needed.

### Data Management
- **Clear Cache:** Free up storage space by clearing cached data from the app.
- **Data Export:** Export your medication history and settings for personal records or to share with healthcare providers.

## Support and Feedback

### Help Center
- **FAQs:** Find quick answers to commonly asked questions about the app and its features.
- **Contact Support:** Reach out to our dedicated support team for assistance with any issues or inquiries.

### Feedback
- **Provide Feedback:** Share your thoughts and suggestions to help us improve your MedInfoHub experience.

## About

### App Information
- **Version:** View the current version of the app and check for updates.
- **Terms of Service:** Access the terms and conditions governing the use of the app.
- **Privacy Policy:** Review our privacy practices to understand how your data is handled.

## Reset App

### Reset Settings
- **Reset to Default:** Restore app settings to the default configuration.

*Thank you for using MedInfoHub. Your health is our priority.*

[Back to Home](#) *Insert link to return to the home screen*

"""

