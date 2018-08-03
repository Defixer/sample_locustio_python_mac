from locust import HttpLocust, TaskSet, task
import json
import random

class UserBehavior(TaskSet):
	def on_start(self):
		""" on_start is called when a Locust start before 
			any task is scheduled
		"""
		self.login()

	def login(self):
		payload = {"grant_type": "password",
				  "username": "crmonline12",
				  "password": "Password01",
				  "client_id": "sugar",
				  "platform": "base",
				  "client_secret": "",
				  "current_language": "en_us",
				  "client_info": {
				    "current_language": "en_us"
				  }
				}
		headers = {'content-type': 'application/json'}
		response = self.client.post("/rest/v10/oauth2/token", data=json.dumps(payload), headers=headers, catch_response=True)
		self.token = response.json()["access_token"]

	# @task(1)
	# def index(self):
	# 	headers = {'oauth-token': self.token}
	# 	self.client.get("/", headers=headers)

	# @task(1)
	# def fetch_accounts(self):
	# 	headers = {'oauth-token': self.token}
	# 	response = self.client.get("/rest/v10/Accounts", headers=headers)

	# @task(1)
	# def fetch_leads(self):
	# 	headers = {'oauth-token': self.token}
	# 	response = self.client.get("/rest/v10/Leads", headers=headers)

	@task(1)
	def create_accounts(self):
		headers = {'oauth-token': self.token}
		payload = {  		   					#request body only needs the "required" fields
		   "nature_of_business_c":"BFB",
		   "industry":"9600",		  
		   "name":"sample org{}".format(random.randint(0,1000))
		}
		response = self.client.post("/rest/v10/Accounts", data=json.dumps(payload), headers=headers)
		
class WebsiteUser(HttpLocust):
	host = 'https://bpiuat.crmonline.com.au'
	task_set = UserBehavior
	min_wait = 5000
	max_wait = 9000