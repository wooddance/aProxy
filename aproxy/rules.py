
COMMON_TASKS = [
    {
        'name': 'xici',
        'test': 'xicidaili.com',
        'resource': ['http://www.xicidaili.com/nn/%s' % i for i in range(1, 6)] +
                    ['http://www.xicidaili.com/wn/%s' % i for i in range(1, 6)] +
                    ['http://www.xicidaili.com/wt/%s' %
                        i for i in range(1, 6)],
        'enable':0,

    },
    {
        'name': 'kuaidaili',
        'test': None,
        'resource': ['https://www.kuaidaili.com/free/inha/%s' % i for i in range(1, 6)] +
                    ['https://www.kuaidaili.com/proxylist/%s' %
                        i for i in range(1, 11)],
        'enable':0,
    },
    {
        'name': 'mrhinkydink.com',
        ''
        'resource': ['http://www.mrhinkydink.com/proxies.htm'],
        'enable':1,
    },
]