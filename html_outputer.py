"""
Html输出器
"""


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        """
        收集数据
        :param data:
        :return:
        """
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        """
        将收集结果输出成Html页面
        :return:
        """
        file_out = open('./output/output.html', 'w')
        file_out.writelines(['<html>\n', '<head>\n'])
        file_out.writelines('<link rel="stylesheet" type="text/css" href="./style.css" />\n')
        file_out.writelines(['</head>\n', '<body class="g-wrap">\n'])
        for data in self.datas:
            file_out.writelines('<div class="g-info">\n')
            file_out.writelines(
                '<p class="m-tt"><a target="_blank" href="%s">%s</a></p>\n' % (data['url'], data['title']))
            file_out.writelines(['<p class="summary">%s</p>\n' % data['summary'], '</div>\n'])
        file_out.writelines(['</body>\n', '</html>'])
        file_out.close()
