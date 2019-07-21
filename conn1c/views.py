from django.shortcuts import render

import requests
import os
import json

user1c = 'web'
pass1c = 'web'

class conn1c:
    base_url = 'http://46.174.89.208:6060/Inwike/hs/Inwike/ID/'

    def load_dict(self, params, data):
        result = {}
        for key in params:
            result[key]=data[key]
        return result

    def load_list(self, prefix, start, data):
        result = []
        cnt = start
        key = '{}_{}'.format(prefix,cnt)
        while key in data:
            result.append(data.get(key,0))
            cnt += 1
            key = '{}_{}'.format(prefix, cnt)
        return result

    def list_proj(self, org_uid):
        payload = {'org_id': org_uid}
        r = requests.get(self.base_url+'list_proj', params=payload, auth=(user1c, pass1c))
        try:
            data = r.json()
        except:
            data = {}

        print(data)
        result=data

        return result

    def list_exec(self, org_uid):
        payload = {'org_id': org_uid}
        r = requests.get(self.base_url+'list_exec', params=payload, auth=(user1c, pass1c))
        try:
            data = r.json()
        except:
            data = {}

        print(data)
        result=data

        return result

    def emp_data(self, emp_UID):
        payload = {'emp_UID': emp_UID}
        r = requests.get(self.base_url+'emp_data', params=payload, auth=(user1c, pass1c))
        try:
            data = r.json()[0]
        except:
            data = {}

        result={}
        result['params'] = self.load_dict(['emp','Dep','org', 'position'], data)

        return result


    def get_uid(self, login, password):
        payload = {'login': login, 'password':password}
        r = requests.post(self.base_url+'get_uid_org', data=json.dumps(payload), auth=(user1c, pass1c))
        try:
            data = json.loads(r.text)
        except:
            data = {}

        result = data
        return result

    def get_photo(self, emp_UID):
        payload = {'emp_UID': emp_UID}
        r = requests.get(self.base_url+'get_foto', params=payload, auth=(user1c, pass1c))
        try:
            data = r.json()[0]
        except:
            data = {}

        photo = data.get('file_foto','')
        return photo

    def upload_photo(self, emp_UID, dstr):
        data = {'uid': emp_UID, 'file': dstr}
        print(data)
        r = requests.post(self.base_url+'upload_foto', data=data, auth=(user1c, pass1c))
        print('Uploaded ?? =>', r)
        return

