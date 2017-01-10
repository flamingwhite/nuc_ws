from SqlUtil import SQLAccess

dbaccess = SQLAccess(host='sweetpi', db='wind')


# with dbaccess.selectall('joke') as jokes:
#     print(jokes)


def sqljokes(n=5):
    with dbaccess.selectall('joke') as jokes:
        fresh = sorted([(id, content, order) for id, content, used, order in jokes if used is 0], key=lambda n: -n[2])[
                :n]
    for id, content, order in fresh:
        with dbaccess.executeSql('update joke set used = 1 where id={}'.format(id)):
            pass
    return [content for _, content, _ in fresh]

