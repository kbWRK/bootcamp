import sys

def main():
    user_total_time_count = {}
    user_login_time = {}
    with open(sys.argv[1], encoding = "utf-8") as f:
        for line in f:
          username, action, timestamp =  line.strip().split(";")
          timestamp = int(timestamp)
          print(username, action, timestamp)
          if action == "LOGIN":
              user_login_time[username] = timestamp
          elif action == "LOGOUT":
              time_in_session = timestamp - user_login_time[username]
              if username in user_total_time_count:
                 user_total_time_count[username] += time_in_session

              else:
                  user_total_time_count[username] = time_in_session
        for user, time in user_total_time_count.items():
            print(f"user{user}")


if __name__ == '__main__':
     ...