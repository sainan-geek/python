unconfirm_users=['alice','brian','candance']
confirmed_users=[]
while unconfirm_users:
    current_user=unconfirm_users.pop()
    print("Verifying user: "+current_user.title())
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
