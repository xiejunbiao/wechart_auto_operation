from pymysql import Connection


msg = {'host': '39.107.69.132',
       'user': 'root',
       'password': 'a123456!',
       'db': 'wechart'}


class GetData(object):
    def __init__(self):
        self.sentence_min = 4
        self.sentence_max = 'POSITIVE_INFINITY'
        self.num = 1000
        self.mysql_conf = msg
        self.conn = Connection(self.mysql_conf['host'],
                               self.mysql_conf['user'],
                               self.mysql_conf['password'],
                               self.mysql_conf['db'])
        self.cur = self.conn.cursor()
        self.sql_select = """
                            select title, content 
                            from poetry
                            where sentence_num BETWEEN {} AND {}
                            ORDER BY  RAND()
                            limit {}
                          """

    def get_data(self, return_num: 'int > 0' = 1000,
                 sentence_num_min: 'int > 0' = 4,
                 sentence_num_max: 'int > sentence_num_min' = 9999999):
        """

        :param return_num:
        :param sentence_num_min: 需要返回的诗词一共多少句
        :param sentence_num_max:
        :return:
        """
        self.num = return_num
        self.sentence_min = sentence_num_min
        self.sentence_max = sentence_num_max
        return self._get_poetry()

    def _get_poetry(self):
        """

        :return:
        """
        self.cur.execute(self.sql_select.format(self.sentence_min, self.sentence_max, self.num))
        data = self.cur.fetchall()

        data_list = []
        for each_ in data:
            data_list.append({'title': each_[0], 'content': each_[1]})
            print({'title': each_[0], 'content': each_[1]})
        print(len(data_list))
        return data_list


if __name__ == '__main__':
    gd = GetData()
    gd.get_data()
