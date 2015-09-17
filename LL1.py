class task:
    c=["S>A B c"
      ,"A>b A"
       ,"A>E"
       ,"B>c"

    ]
    null_nonterminal=[]
    BDW=[]
    mat=[]
    null_nonrule=[]
    DEO=[]
    spec_word=[")","(","+","*","&","-","/"]
    def take_input(self):
        for x in self.c:
           va=x.split(">")
           asd=va[1].split(" ")
           b=[]
           b.append(va[0])
           b.append(asd)
           self.mat.append(b)
    def step1(self):
        index=0
        for x in self.mat:
            if 'E' in x[1]:
                self.null_nonrule.append(index)
                self.null_nonterminal.append(x[0])
            index=index+1

        for z in self.mat:
            test=0
            for w in z[1]:
                for f in w:
                   if not f in self.null_nonterminal:
                      test=1
            if test ==0:
                self.null_nonterminal.append(z[0])
    def step2(self):
        index=0
        for w in self.mat:
            if not (index in self.null_nonrule):
                for m in w[1]:
                    if not  m in self.null_nonterminal:
                        a=[]
                        a.append(w[0])
                        a.append(m)
                        if not(a in self.BDW):
                          self.BDW.append(a)
                        break
                    else:
                        a=[]
                        a.append(w[0])
                        a.append(m)
                        if not(a in self.BDW):
                           self.BDW.append(a)



            index=index+1
    def step3(self):
        self.BW=[]
        a=[]
        b=[]
        self.mm=[]
        for n in self.BDW:
            ww=[]
            ww.append(n[0])
            ww.append(n[1])
            if not(ww in self.BW):
                self.BW.append(ww)
        for n in self.BDW:
            a.append(n[0])
            b.append(n[1])
        for t in self.mat:
            if not (t[0] in self.mm):
                self.mm.append(t[0])
            for n in t[1]:
                if not(n in self.mm) and not  n in 'E' :
                    self.mm.append(n)
        ar=0
        indd=0
        while ar==0:
            ar=-1
            vv=len(a)
            while(indd<vv):
               indices = [i for i, x in enumerate(a) if x == b[indd]]
               for t in indices:
                   wr=[]
                   wr.append(a[indd])
                   wr.append(b[t])
                   if not(wr in self.BW):
                      a.append(wr[0])
                      b.append(wr[1])
                      ar=0
                      self.BW.append(wr)
               indd=indd+1


        for w in self.mm:
            k=[]
            k.append(w)
            k.append(w)
            if not( k in self.BW):
               self.BW.append(k)
    def step4(self):
        self.First=[]
        for x in self.mm:
            a=[]
            for w in self.BW:
                if x ==w[0] and (w[1].islower() or (w[1] in self.spec_word)):
                   a.append(w[1])
            ter=[]
            ter.append(x)
            ter.append(a)
            self.First.append(ter)

    def step5(self):
        self.dict={}
        self.FirstR=[]
        for b in self.First:
            self.dict[b[0]]=b[1]
        for a in self.mat:
            m=[]
            for x in a[1]:
                if not x in self.null_nonterminal:
                    if x in self.dict:
                        tt=self.dict[x]
                        for n in tt:
                                m.append(n)
                    break
                else:
                    if x in self.dict:
                        tt=self.dict[x]
                        for n in tt:
                                m.append(n)
            self.FirstR.append(m)
    def step6(self):
        self.FDB=[]
        rt=self.mat[1]
        for n in self.mm:
            for wer in self.mat:
                if n in wer[1] and n.isupper():
                    c=wer[1].index(n)
                    mt=wer[1]
                    c=c+1
                    for p in range(c,len(wer[1])):
                        a=[]
                        a.append(n)
                        a.append(mt[p])
                        if not a in self.FDB:
                           self.FDB.append(a)
                        if not mt[p] in self.null_nonterminal:
                            break

    def step7(self):
        index=0
        for w in self.mat:
            if not (index in self.null_nonrule):
                x=w[1]
                x.reverse()
                for m in x:
                    if not  m in self.null_nonterminal:
                        a=[]
                        a.append(m)
                        a.append(w[0])
                        if not a in self.DEO:
                           self.DEO.append(a)
                        break
                    else:
                        a=[]
                        a.append(m)
                        a.append(w[0])
                        if not  a in self.DEO:
                           self.DEO.append(a)
            index=index+1
        for m in self.mat:
            x=m[1]
            x.reverse()
    def step8(self):
        self.EO=[]
        a=[]
        b=[]
        for x in self.DEO:
            t=[]
            t.append(x[0])
            t.append(x[1])
            self.EO.append(t)
            a.append(x[0])
            b.append(x[1])
        ar=0
        indd=0
        while ar==0:
            ar=-1
            vv=len(a)
            while(indd<vv):
               indices = [i for i, x in enumerate(a) if x == b[indd]]
               for t in indices:
                   wr=[]
                   wr.append(a[indd])
                   wr.append(b[t])
                   if not(wr in self.DEO):
                      a.append(wr[0])
                      b.append(wr[1])
                      ar=0
                      self.EO.append(wr)
               indd=indd+1


        for w in self.mm:
            a=[]
            a.append(w)
            a.append(w)
            if not(a in self.EO):
               self.EO.append(a)
    def step9(self):
        tmp=[]
        self.FB=[]
        for ind in self.EO:
            for ind1 in self.FDB:
                if ind[1] in ind1[0]:
                    a=[]
                    a.append(ind[0])
                    a.append(ind1[1])
                    if not a in tmp:
                       tmp.append(a)
        for inn in tmp:
            for we in self.BW:
                if inn[1] in we[0]:
                    a=[]
                    a.append(inn[0])
                    a.append(we[1])
                    if not a in self.FB:
                       self.FB.append(a)
    def step10(self):
       we=self.mat[0]
       start=we[0]

       for w in self.EO:
           if w[1] ==start and w[0].isupper():
               a=[]
               a.append(w[0])
               a.append('!')
               if not( a in self.FB):
                  self.FB.append(a)
    def step11(self):
        self.Fol=[]
        for x in self.null_nonterminal:
            a=[]
            for z in self.FB:
                if x in z[0] and (z[1].islower() or z[1] in self.spec_word) and not (z[1] in a) :
                    a.append(z[1])
            w=[]
            w.append(x)
            w.append(a)
            self.Fol.append(w)
    def step123(self):
        self.dict1={}
        for a in self.Fol:
            w=[]
            for z in a[1]:
                w.append(z)
            self.dict1[a[0]]=w


    def step12(self):
        self.an=[]
        for index in range(0,len(self.c),1):
            if index in self.null_nonrule:
                tmp=self.mat[index]
                self.an.append(self.dict1[tmp[0]])

            else:
                self.an.append(self.FirstR[index])
    def determiner(self):
        ter=0
        for x in self.mat:
            va=x[1]
            if x[0] in va[0]:
                ter=1
        if ter==0:
            print('In LL(1)')
        else:
            print('None in  LL(1)')





    def steps(self):
        self.take_input()
        self.step1()
        print('Non Terminals  are',self.null_nonterminal)
        print('NuLLalbe Rules',self.null_nonrule)
        self.step2()
        print('BDW')
        for x in self.BDW:
            print( x[0],'BDW',x[1])
        self.step3()
        print('BW')
        for x in self.BW:
            print( x[0],'BW',x[1])
        print('First')
        self.step4()
        for x in self.First:
            print(x)
        print('FirstR')
        self.step5()
        for x in self.FirstR:
            print(x)

        if len(self.null_nonterminal)>0:
            self.step6()
            print('FDB')
            for x in self.FDB:
                print( x[0],'FDB',x[1])

            self.step7()
            print('DEO')
            for x in self.DEO:
                print( x[0],'DEO',x[1])
            self.step8()
            print('EO')
            for x in self.EO:
                print( x[0],'EO',x[1])
            self.step9()
            print('FB')
            for x in self.FB:
                print( x[0],'FB',x[1])
            self.step10()
            print('FB')
            for x in self.FB:
                print( x[0],'FB',x[1])
            self.step11()
            print('FOL')
            for x in self.Fol:
                print( x[0],'FOL',x[1])
            self.step123()
        self.step12()
        print('Selection')
        for x in self.an:
            print(x)

ass=task()
ass.steps()
ass.determiner()
#print("bdw")
#print(ass.BDW)
#print("bw")
#print(ass.BW)
#print("FIRST")
#print(ass.First)
#print("FIRSTR")
#print(ass.FirstR)
#print(ass.EO)
#print(ass.FDB)
#print(ass.Fol)