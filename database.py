client = {'672192983': {'name': 'brandon',
                        'id': 'AA1877392',
                        'acount_type': 'normal',
                        'account_balance': 50000,
                        
                        },
          
          '670002814': {'name': 'peter',
                    'id': 'TT4353758',
                    'machan code': 'GTS45',
                    'acount_type': 'seller',
                    'account_balance': 55000,
                    },
          
          '670012814': {'name': 'bob',
                    'id': 'TT4353758',
                    'machan code': 'GTS65',
                    'acount_type': 'comecial',
                    'account_balance': 70000,
                    },
          
          '652581620': {'name': 'john',
                        'id': 'AA1877402',
                        'acount_type': 'normal',
                        'account_balance': 80000,
                    }
          }

transaction = {
    'AA1877392': {
        "07/25/2026": {'time': '12:30 Pm',
                       'action': 'withdraw',
                       'machan': "GTS45", # this go to callboxer Peter
                       'transaction_id': 'DX5386631',
                        'amount': 3000                 
        },
        
        "07/20/2026": {'time': '12:30 Pm',
                       'action': 'withdraw',
                       'machan': "GTS65",  #callboxer peter
                       'transaction_id': 'DX53866541',
                        'amount': 2000    
        },
        "07/17/2026": {'time': '12:30 Pm',
                       'action': 'transfer',
                       'machan': "none",
                       'transaction_id': 'DX53945631',
                        'amount': 1000
        },
    },
    
    'TT4353758': {
        "07/25/2026": {'time': '12:33 Pm',
                       'action': 'withdraw',
                       'machan': "GTS45", # this go to callboxer Peter
                       'transaction_id': 'DX5376631',
                        'amount': 3000                 
        },
    }
}


print(client)
