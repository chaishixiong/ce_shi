class ProcessingText(object):
    def __init__(self):
        self.data = ''
        self.num = 1

    def read_data(self):
        with open('feng_lan_spider/call_log_text.txt', 'r', encoding='utf-8')as f:
            for i in f:
                #
                with open('feng_lan_spider/new_call_log_text.txt', 'a', encoding='utf-8')as f_write:
                    if self.num == 1:
                        f_write.write(i.strip())
                        self.data = i.strip()
                    elif i.strip()[:4:1] == self.data.strip()[:4:1]:
                        f_write.write('\n')
                        f_write.write(i.strip())
                        self.data = i.strip()
                    elif i == '\n' or i == ',':
                        print('-------------------空格-------------------')
                    else:
                        with open('feng_lan_spider/new_call_log_text.txt', 'a', encoding='utf-8')as f_write:
                            f_write.write('。' + i.strip())
                            self.data = self.data + '。' + i.strip()
                self.num += 1


if __name__ == '__main__':
    r = ProcessingText()
    r.read_data()
