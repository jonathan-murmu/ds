mappings = {
  "user": {
    "google": {
      "name": "displayName",
      "first_name": "firstName",
      "last_name": "lastName",
      "personal_email": "email"
    },
    "okta": {
      "user_name": "displayName",
      "firstname": "firstName",
      "lastname":  "lastName",
      "business_email": "email"
    }
  }
}

schema = 'user'
provider = "google"

temp = mappings[schema][provider]
print(temp)

new_temp = {}
for k,v in temp.items():
    new_temp[v] = k

print(new_temp)