import requests

def main():
    valid_tokens = []
    while True:
        token = input("Enter a Discord token (or type 'exit' to quit): ").strip()
        
        if token.lower() == 'exit':
            break
        
        headers = {'Authorization': token, 'Content-Type': 'application/json'}
        requ = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
        
        if requ.status_code == 401:
            print("Token is invalid:", token)
        elif requ.status_code == 200:
            valid_tokens.append(token)
            json = requ.json()
            print("Valid Token:")
            print("  Token:", token)
            print("  Email:", json['email'])
            print("  Phone:", json['phone'])
            print("  Username:", f'{json["username"]}#{json["discriminator"]}')
            print("  Nitro:", bool(len(requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers).json()) > 0))
            print("  Billing:", bool(len(requests.get('https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers=headers).json()) > 0))
            print("  Avatar:", f"https://cdn.discordapp.com/avatars/{str(json['id'])}/{str(json['avatar'])}")
            print("  ID:", str(json["id"]))
            print()

    if not valid_tokens:
        print("No valid Discord Tokens")

if __name__ == "__main__":
    main()
