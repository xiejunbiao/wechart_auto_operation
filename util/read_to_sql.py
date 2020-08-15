import pymysql

mysql_conn2 = ['39.107.69.132', 'root', 'a123456!', 'wechart']


def connectmysql(host, user, passwd, database):
    """
    链接一个数据库返回一个游标
    """
    conn = pymysql.Connect(host=host, user=user, password=passwd,
                            database=database)
    return conn


conn_ = connectmysql(mysql_conn2[0], mysql_conn2[1], mysql_conn2[2], mysql_conn2[3])
cur = conn_.cursor()

update_sql = """
        INSERT INTO poetry (
            index_,
            title,
            author,
            dynasty,
            content,
            type_,
            emotional_type,
            words_num,
            sentence_num,
            appreciate,
            picture_type,
            is_picture,
            source,
            introduction_author
        )
        VALUES ({}) 
        ON DUPLICATE KEY UPDATE 
        index_ = VALUES(index_),
        title = VALUES(title),
        author = VALUES(author),
        dynasty = VALUES(dynasty),
        content = VALUES(content),
        type_ = VALUES(type_),
        emotional_type = VALUES(emotional_type),
        words_num = VALUES(words_num),
        sentence_num = VALUES(sentence_num),
        appreciate = VALUES(appreciate),
        picture_type = VALUES(picture_type),
        is_picture = VALUES(is_picture),
        source = VALUES(source),
        introduction_author = VALUES(introduction_author)
    """.format('%s'+',%s'*13)
path = r'E:\微信公众号运营管理\data_poetry\poetry.txt'
f = open(path, 'r', encoding='utf-8')
data = f.readlines()
i = 1
data_list = []
for line in data:
    line = line.strip().replace('\t', '').replace('\n', '').split(':')
    print(line[0])
    title = line[0]
    content = line[1]
    words_num = len(content)
    sen_list = line[1].split('。')[:-1]
    sentence_num = len(sen_list)

    data_list.append((i,
                      title,
                      'author',
                      'dynasty',
                      content,
                      'type',
                      'emotional_type',
                      words_num,
                      sentence_num,
                      'appreciate',
                      'picture_type',
                      0,
                      'source',
                      'introduction_author'
                      ))
    i += 1
    # for j in sen_list:
    #     print(j + '。')
print('----------------------------------------------------')
print('一共{}首诗'.format(len(data_list)))
cur.executemany(update_sql, data_list)
conn_.commit()
cur.close()
conn_.close()




