import win32api
import win32security


class ActiveDirectoryConnection():
    def __init__(self) -> None:
        import win32api
        import win32security

        # Get the process handle for the current process
        process_handle = win32api.GetCurrentProcess()

        # Get the token handle for the process
        token_handle = win32security.OpenProcessToken(
            process_handle, win32security.TOKEN_READ)

        # Get the SID for the current user
        user_sid = win32security.GetTokenInformation(
            token_handle, win32security.TokenUser)[0]

        # Get the user object from Active Directory using the user's SID
        user_obj = win32security.LookupAccountSid(None, user_sid)

        # Print the user's domain, username, and full name
        print(
            f"Domain: {user_obj[0]}\nUsername: {user_obj[1]}\nFull Name: {user_obj[2]}")
