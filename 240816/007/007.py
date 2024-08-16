class SecretMeeting:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time
    
    def display_info(self):
        print(f"secret code : {self.secret_code}")
        print(f"meeting point : {self.meeting_point}")
        print(f"time : {self.time}")

secret_code, meeting_point, time = input().split()

meeting = SecretMeeting(secret_code, meeting_point, time)

meeting.display_info()