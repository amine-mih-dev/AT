import unittest
import requests

client_test_data = [
    {'idc': 1,
     'name': 'John',
     'prename': 'Doe',
     'birthday': '1990-01-01',
     'idcard': '1',
     'releasecrd': '2010-01-01',
     'Phone': '00001',
     'email': 'john.doe@example.com'
     },
    {'idc': 2,
     'name': 'Jane',
     'prename': 'Doe',
     'birthday': '1991-01-01',
     'idcard': '2',
     'releasecrd': '2010-01-01',
     'Phone': '00002',
     'email': 'jane.Doe@example.com'
     }, {
        'idc': 3,
        'name': 'zakzok',
        'prename': 'Doe',
        'birthday': '1993-01-01',
        'idcard': 'ty',
        'releasecrd': '2012-01-01',
        'Phone': '00003',
        'email': 'zakzok@example.com'

    }
]
client_put_data = {
    'idc': 1,
    'name': 'amine',
    'prename': 'De',
    'birthday': '1999-09-09',
    'idcard': '4',
    'releasecrd': '2022-03-28',
    'Phone': '213678',
    'email': 'aminemih@gmail.com'
}
convention_test_data = [
    {'idcv': 1,
     'namecv': 'Convention 1',
     'remise': 1,
     },
    {'idcv': 2,
     'namecv': 'Convention 2',
     'remise': 2,
     }, {
        'idcv': 5,
        'namecv': 'Convention 5',
        'remise': 5,

    }
]
transform_test_data = [
    {'idt': 1,
     'street1': 'street 1',
     'street2': 'street 2',
     'date': '2010-01-01',
     'idl': 1,
     },
    {'idt': 2,
     'street1': 'street 2',
     'street2': 'street 3',
     'date': '2010-01-01',
     'idl': 2,

     },
    {'idt': 3,
     'street1': 'street 3',
     'street2': 'street 4',
     'date': '2010-01-01',
     'idl': 3,
     }, ]

cession_test_data = [
    {'idcs': 1,
     'date': '2010-01-01',
     'idl': 1,
     'ces': 1,
     },
    {'idcs': 2,
     'date': '2010-01-01',
     'idl': 1,
     'ces': 2,
     },
    {'idcs': 3,
     'date': '2010-01-01',
     'idl': 2,
     'ces': 3,
     }, ]
line_test_data = [
    {'idl': 1,
     'numberl': '1',
     'street': 'street 1',
     'date': '2010-01-01',
     'idc': 1,
     'serv': 1,
     },
    {'idl': 2,
     'numberl': '2',
     'street': 'street 2',
     'date': '2010-01-01',
     'idc': 2,
     'serv': 2,
     }, {
        'idl': 3,
        'numberl': '3',
        'street': 'street 3',
        'date': '2010-01-01',
        'idc': 3,
        'serv': 3,
    }]

legit_mock_data = [{'id': 4,
                    'date': '2040-01-01',
                    'namepr': 'promo',
                    'typepr': 'teepee',
                    'namecv': 'Convocation',
                    'numberl': '2',
                    'street': 'street fighter',
                    }]
history_test_data = [
    {'id': 1,
     'idc': 1,
     'idl': 1,
     'date': '2010-01-01',
     'idp': 1,
     'idcv': 1,
     'idtr': 1,
     'idcs': 1,
     },
    {'id': 2,
     'idc': 2,
     'idl': 2,
     'date': '2010-01-01',
     'idp': 2,
     'idcv': 2,
     'idtr': 2,
     'idcs': 2,
     },
    {'id': 3,
     'idc': 3,
     'idl': 3,
     'date': '2010-01-01',
     'idp': 3,
     'idcv': 3,
     'idtr': 3,
     'idcs': 3,
     }, {
        'id': 4,
        'idc': 1,
        'idl': 2,
        'date': '2040-01-01',
        'idp': 1,
        'idcv': 2,
        'idtr': 1,
        'idcs': 2,
    }]

promotion_test_data = [
    {'idp': 1,
     'namepr': 'Promotion 1',
     'typepr': 'type 1',
     'mountpr': 'mount 1',
     },
    {'idp': 2,
     'namepr': 'Promotion 2',
     'typepr': 'type 2',
     'mountpr': 'mount 2',
     },
    {'idp': 3,
     'namepr': 'Promotion 3',
     'typepr': 'type 3',
     'mountpr': 'mount 3',
     }
]

URL = 'http://127.0.0.1:5000/'


class MyTestCase(unittest.TestCase):
    '''    def test_client(self):
        for client in client_test_data:
            r = requests.post(URL + 'client', json=client)
            get_r = requests.get(URL + 'client', json={'idc': client['idc']})
            self.assertEqual(r.status_code, 200)
            self.assertEqual(get_r.status_code, 200)
            self.assertEqual(get_r.json(), client_put_data)
            put_r = requests.put(URL + 'client', json=client_put_data)
            get_r = requests.get(URL + 'client', json={'idc': client_put_data['idc']})
            self.assertEqual(put_r.status_code, 200)
            self.assertEqual(get_r.status_code, 200)
            self.assertEqual(get_r.json(), client_put_data)'''
    def test_get_empty_numbers(self):
        r = requests.get(URL + 'empty_number')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json(), [])


if __name__ == '__main__':
    unittest.main()
