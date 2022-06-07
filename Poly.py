class Poly:
    def __init__(self, poly, letter, cs=None):
        self.l = letter
        if cs:
            self.dic = cs
            return

        poly = poly.replace(' ', '').replace(
            '+', ' +').replace('-', ' -').split()
        dic = {}
        for i in poly:
            if letter not in i:
                dic[0] = dic.get(0, 0) + int(i)
                continue
            if '**' not in i:
                i += '**1'
            j = i.split('**')
            j[0] = j[0].split('*')
            dic[int(j[1])] = dic.get(int(j[1]), 0) + int(j[0][0])
        self.dic = dic

    def __add__(self, other):
        d = self.dic
        dd = other.dic
        dic = {}
        for i in {*d.keys(), *dd.keys()}:
            dic[i] = d.get(i, 0) + dd.get(i, 0)
        for i in [*filter(lambda i: not dic.get(i), dic)]:
            del dic[i]
        return Poly('', self.l, cs=dic)

    def __mul__(self, other):
        d = self.dic
        dd = other.dic
        dic = {}
        for i in d:
            for j in dd:
                dic[i+j] = dic.get(i+j, 0) + d[i] * dd[j]
        for i in [*filter(lambda i: not dic.get(i), dic)]:
            del dic[i]
        return Poly('', self.l, cs=dic)

    def __sub__(self, other):
        d = self.dic
        dd = other.dic
        dic = {}
        for i in {*d.keys(), *dd.keys()}:
            dic[i] = d.get(i, 0) - dd.get(i, 0)
        for i in [*filter(lambda i: not dic.get(i), dic)]:
            del dic[i]
        return Poly('', self.l, cs=dic)

    def __divmod__(self, other):
        d = self.dic
        dd = other.dic
        dic = {}
        dmax = max(d)
        ddmax = max(dd)
        while dmax >= ddmax:
            dic[dmax - ddmax] = dic.get(dmax - ddmax, 0) + d[dmax]//dd[ddmax]
            d = Poly.__sub__(self, other*Poly('', self.l, cs=dic)).dic
            try:
                dmax = max(d)
            except:
                break
            ddmax = max(dd)
        return Poly('', self.l, cs=dic), Poly('', self.l, cs=d)

    def __repr__(self):
        dic = self.dic
        for i in [*filter(lambda i: not dic.get(i), dic)]:
            del dic[i]
        self.dic = dic
        s = ''
        for i, j in sorted(dic.items())[::-1]:
            s += '' if j < 0 else '+'
            if i != 0:
                s += f'{j}*{self.l}'
                s += (f'**{i}') if i != 1 else ''
                continue
            s += str(j)
        if s:
            return s
        return '0'

    def __str__(self):
        return self.__repr__()

    def derivative(self):
        d = self.dic
        d[0] = 0
        dic = {}
        for i in d:
            dic[i-1] = i*self.dic[i]
        return Poly('', self.l, cs=dic)
