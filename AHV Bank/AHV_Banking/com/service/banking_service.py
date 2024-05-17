
from AHV_Banking.com.repo.db_operations import *

# function to fetch userId based on user_email
def fetch_userID(user_mail):

    # fetching entire row based on email from ahv_users
    db_data_users = fetch_data('ahv_users', email=user_mail)
    try:
        # fetching userId variable from entire row
        userId = db_data_users[0][0]
        return userId

    except:
        return False


def displayBalance(user_mail):

    #fetching userId based on user_mail from ahv_users table
    userId = fetch_userID(user_mail)

    if userId:
        db_data_accounts = fetch_data('ahv_accounts', user_id=userId)
        print("[+] Account Balance: " + str(db_data_accounts[0][3]))
        print()
        return True

    else:
        return False


def depositMoney(user_mail,depositAmount):

    # fetching userId based on user_mail from ahv_users table
    userId = fetch_userID(user_mail)

    if userId:
        try:
            # fetching entire row of ahv_accounts table based on userId
            db_data_accounts = fetch_data('ahv_accounts', user_id=userId)

            # extracting and updating balance variable from entire row
            balance = db_data_accounts[0][3] + depositAmount

            # updating balance variable in database, ahv_accounts table using userId
            update_data('ahv_accounts', values={'balance': balance}, conditions={'user_id': userId})
            displayBalance(user_mail)

            return True

        except:

            return False
    else:

        return False

def withdrawlMoney(user_mail,withdrawlMoney):

    # fetching userId based on user_mail from ahv_users table
    userId = fetch_userID(user_mail)

    if userId:

        # fetching entire row of ahv_accounts table based on userId
        db_data_accounts = fetch_data('ahv_accounts', user_id=userId)

        # extracting user balance from entire row data
        balance = db_data_accounts[0][3]

        # function to check whether user balance is greater than withdrawlamount
        if balance > withdrawlMoney:
            balance = balance - withdrawlMoney

            # updating new user balance into database
            update_data('ahv_accounts', values={'balance': balance}, conditions={'user_id': userId})
            displayBalance(user_mail)
            return True

        else:
            print("[-] Insufficient Funds...")
            print()
            return False

    else:
        return False


def transferMoney(user_mail,transferAmount):

    # fetching senderUserId based on user_mail from ahv_users table
    senderUserId = fetch_userID(user_mail)

    # fetching account information from senderUserId from ahv_accounts table
    senderAccountDetails = fetch_data('ahv_accounts', user_id=senderUserId)

    # extracting senderDetails from ahv_accounts table
    senderBalance = senderAccountDetails[0][3]
    senderAccountId = senderAccountDetails[0][0]
    senderAccountNumber = senderAccountDetails[0][2]

    # checking whether senderBalance is greater than amount to be transferred
    if senderBalance > transferAmount:

        # receiver accountId
        receiverAccountId = int(input("Enter Recepients Account Id: "))
        #account_ids = fetch_column_data('ahv_accounts', 'account_id')

        # checking whether receiver account does exist or not
        if receiverAccountId in fetch_column_data('ahv_accounts', 'account_id'):

            # performing update operations on sender account balance
            UptSenderBalance = senderBalance - transferAmount

            # updating new sender account info into ahv_accounts database
            update_data('ahv_accounts', values={'balance': UptSenderBalance}, conditions={'user_id': senderUserId})
            displayBalance(user_mail)

            # fetching receiver account info from ahv_accounts
            receiver_db_data = fetch_data('ahv_accounts', account_id=receiverAccountId)

            # extracting receiver data
            receiverUserId = receiver_db_data[0][1]
            receiverAccountNumber = receiver_db_data[0][2]

            # performing update operations on receiver account balance
            receiverBalance = receiver_db_data[0][3] + transferAmount

            # updating receiver account info into database
            update_data('ahv_accounts', values={'balance': receiverBalance}, conditions={'account_id': receiverAccountId})



            # inserting transaction details into ahv_transactions table (sender side)
            insert_data('ahv_transactions', user_id=senderUserId, account_id=senderAccountId, amount=transferAmount, from_account=senderAccountNumber,
                        to_account=receiverAccountNumber, trans_type='db')


            # inserting transaction details into ahv_transactions table (sender side)
            insert_data('ahv_transactions', user_id=receiverUserId, account_id=receiverAccountId, amount=transferAmount,
                        from_account=senderAccountNumber,
                        to_account=receiverAccountNumber,trans_type='cd')

            return True

        else:
            print("[-] Receiver Account Do not exist..")
            print()
            return False

    else:
        print("[-] Insufficient Balance..")
        print()
        return False

def transactionHistory(user_email):
    try:
        # Connect to the MySQL database
        conn = db_connect()

        # Create a cursor to execute SQL queries
        cursor = conn.cursor()

        # Query to retrieve transaction history based on user email
        query = """
                SELECT ahv_users.first_name, ahv_users.last_name, ahv_accounts.account_number, ahv_transactions.amount, ahv_transactions.from_account, ahv_transactions.to_account, ahv_transactions.trans_date, ahv_transactions.trans_type
                FROM ahv_users
                INNER JOIN ahv_transactions ON ahv_users.user_id = ahv_transactions.user_id
                INNER JOIN ahv_accounts ON ahv_transactions.account_id = ahv_accounts.account_id
                WHERE ahv_users.email = %s
            """

        # Execute the query with the provided user_email
        cursor.execute(query, (user_email,))

        # Fetch and print the transaction history
        print("Transaction History for User:", user_email)
        print("{:<15} {:<15} {:<20} {:<15} {:<15} {:<15} {:<15} {:<10}".format("First Name", "Last Name",
                                                                               "Account Number", "Amount",
                                                                               "From Account", "To Account", "Date",
                                                                               "Trans Type"))
        for row in cursor.fetchall():
            first_name, last_name, account_number, amount, from_account, to_account, trans_date, trans_type = row
            print(
                "{:<15} {:<15} {:<20} {:<15} {:<15} {:<15} {:<15} {:<10}".format(first_name, last_name, account_number,
                                                                                 amount, from_account, to_account, str(trans_date),
                                                                                 trans_type))

        print()
        # Close the cursor and the database connection
        cursor.close()
        conn.close()

        return True

    except mysql.connector.Error as e:
        #
        # baprint("Error:", e)
        return False




