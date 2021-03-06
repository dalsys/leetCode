import re
class Solution:
    def wordBreak2(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        pattern = '^({})*$'.format('|'.join(wordDict))
        return bool(re.match(pattern, s))

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return True
        if not wordDict:
            return False

        wordDict = set(wordDict)

        l, r = 0 ,1
        breaks = []
        success, fail = set([]), set([])
        while l>=0 and r<= len(s):
            # print((s[:l],s[l:r],s[r:]), (l, r), breaks, success, fail)
            if r in success:
                r+=1
            elif l in fail:
                if not breaks:
                    return False
                r = breaks.pop()+1
                l = breaks[-1] if breaks else 0
            elif s[l:r] in wordDict:
                if r == len(s):
                    return True
                breaks.append(r)
                success.add(r)
                l = r
                r += 1
            elif r == len(s):
                if not breaks:
                    return False
                fail.add(l)
                r = breaks.pop()+1
                l = breaks[-1] if breaks else 0
            else:
                r += 1

        return False


if __name__ == '__main__':
    solution = Solution()
    # s = 'foobar'
    # wordDict = ["f","fo", 'foo','dar' ,'foobar']
    # s = 'aaaab'
    # wordDict = ["a","aa"]
    # s = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'
    # wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    # # s = "aaaaaaa"
    s = "catsandog"
    wordDict = ["cats", "dog", "and", "cat"]
    # s = "fajbeokiakfmlacbinjdnjdmmfha"
    # wordDict = ["be","ellaekgjhibcomc","ahaklkan","jcm","lchidklmcone","ljmdgagaen","giioojldjkfnno","el","eibjaffacjll","hn","hbjakhjneml","foi","nbhf","aigf","cfdlnc","fa","amakgofedhkghgl","ddhmhdhioh","ijoddeabbiei","giamcgco","nholghlfbbendi","emlc","m","elgibme","behkignjenmh","lodkkjgioe","doe","hgflgakna","macghogdidmdm","ec","kncigolkog","ljooio","lch","gkaclkbjn","ofiaglfoffl","alhfbb","cfmdbgo","cfcnajknk","jfh","almbgdjnbbbgmhb","dmlnnohf","olojeejfafc","ndgcmgoe","cmkdjilfeo","bengdd","enfg","dbngiggni","anmkljn","njdnjdmmfha","ndimmddfmhe","hmkdjkhhiilnf","ehd","jfdl","dlgki","bhoflnomibkki","lg","fjojjnnkdfenhol","lefhhl","nimdl","gejgomblmim","ahbnlmlfmejjj","glhacaojnf","mfjdhnhdkm","do","fnh","mnmjdk","hfjgdlnnb","hniolfhkhbie","ldgodonogcab","mabjnnohnijhn","aceojlkmdg","aedfljg","cehk","jag","oniegflnhje","jo","maokc","jkbndc","djbn","dajkdblojkf","dmen","kcdjdocinenc","cgindbm","h","odaof","cmogcbgj","anjahlgbbmba","haoe","ggacnminj","ilcfjoedhe","klookammgofl","onnmenn","mbdneaioo","jc","dekgil","bjdfibfd","hfbnlgmlllcb","afebehf","obekljbnh","eoaedhjk","nobamccd","mdieojoknf","komcglmakkaa","jcliimcc","jmmgbmha","gdogjnn","ednembco","dgno","jiaheeabifahfmo","djkcgnakkh","kdkiglgf","eb","fmdnlhj","eicohdciejc","jgofmankkf","o","nnmomkmkmiaoga","njchkccln","ndamha","eleanmojdi","ebkl","jcageehlelcg","acfddofjihgmn","iklaomfhjm","io","igmob","lfnhnlnigbbignk","anihfojmedf","nj","oilcabalhb","adjfbkfjch","lbfb","mgfnngfccb","jhmhggm","dnllc","c","ljim","jmikd","mdfimdgac","fhbclgo","edclcdia","nelmfjejff","i","cmcbbckdnjcoo","cddocce","hc","keh","keofhnhemd","biln","mjcnbjmkikon","fekbdnkolahh","hkfmjbj","mjoj","jn","ilof","ifhfk","aofmg","nofljgmmmf","hcdifeiclbchlf","imlijgdg","ocdiiemcmbkglm","nhoekmlkjfoa","kibffkbleedda","kdhdjekccbkc","bcbflcag","jekmkdimnnjjoo","mmgfljchalbem","kchk","oi","ncf","jembgfa","l","kfkeianmmmdacl","ecjkkfggj","jdgcfnhfjonkhig","jhagiokii","nifm","bbjjlj","adajlokomibfg","ojk","lockdel","bh","hoojolglchck","conko","eadi","kfigoijnfimolen","g","dbnj","cojkbmo","hh","mcdbh","ngdmgioen","ehjagfohnolkho","dgfgdlc","aoglneoh","gbc","ijjckddeicld","imekih","liiaecniil","hahejbhgiclb","fnmojm","ablihjhggiahhno","colloaakco","jhobddaanbhmlg","cbfajfhkoh","cim","laghknigabn","dcbnbkegkjam","gem","ljjim","icclogji","omidhe","f","giiaclfcjkagl","ndcjldekjnkekm","aiikdccohcj","mkbmb","oomhhafobic","bkacdjfgbggn","ahghdoahbi","hedm","eeoj","bdgdlfollegej","eg","dfeb","dkffkid","hcne","gjkohnaaabn","jfeododjgdhlfbf","clfkmconnkfb","abnbkcni","hk","ghnmhjm","oibjibmkaibdefa","hjambim","oe","aao","jil","fmhomflfen","hlidcklnmb","hiaonkhd","bibbmkandf","hke","bmfcionm","inhcnlkbkkmjicn","jckjedhgoghi","chmik","mnjldknhaec","hocbccbg","ljadj","lciikgnlj","ifjjhkbhifione","foikblanoco","ode","mjc","fhklofh","mmoklkkog","hocbojmhffeajo","ccmmd","bkkh","nhhgcflniebkme","lfohikenfbjacli","cmehijnihijgng","caa","bmk","emofof","jjagiogohfab","ibh","eoacdlnodalkjbl","cbbjbbnjom","iljiomeloehen","gignlngclmh","b","ll","dokgngnocde","cienegffibgieba","agbachloidg","mlelnafokd","nmcmka","akeogjbjcnf","nebdic","a","efc","ljdk","jhcag","bkbikbjgae","mcjlgjeo","lo","dbiofobl","cehebiljff","eeagngm","ondahcjiel","coblanndhlhoggj","jaobmjml","jfejjinofek","hhnna","gdhcn","acelcomgkgohm","njkkjkkln","jmc","hkekoho","boefec","cioibfgjmhb","ebggdbeimn","emhg","cfghkhii","d","k","khoddedia","nhje","eebkfml","bohhd","kg","n","ilgemokdehcbaif","cldicda","einij","akmabcgfn","fmkmcn","bnlfbagkke","oakbgjejmcncj","iehdfadgoik","kkcfo","jmjkmfcacjjnd","ndokhh","hjfeelhckkjjmj","dnomohejbodkb","jcmblncjadno","oiofcodobiml","ddmillkncjfdfj","aihenmkdnhdhkhf","bfdbakeilfdojnc","jjhbkbne","aigabk","cae","oednojjb","gdoe","jokjceohkmbm","offkanbahigo","kfomigbfddjli","dkkjobgkcejei","mdilld","bofkika","kkinig","cljcflbghjmhmke","kmbjlgdcbdjn","bkgbmoahda","kmnajjdemggnfg","mgjndldil","iemb","kehaokgjg","icign","oijmaolehmoo","amhgldifmgekhe","diacnollhi","lnjhdaafadl","bdfiackhogoje","ebjlfa","deabkgfhnead","gadcob","haa","dbhnbhjcmmab","bbmjainilbbej","dc","bgjgafnjjflne","ehholgnn","fmhccbnc","mdnfl","feeejdgc","mfhlobdadooh","ojna","gkgjnijdbgo","ghngnhn","nhnjaiaadiedgg","nk","hmd","nmbmijaffogl","onkcgbgmago","gfli","ofjlec","nlfnbkkdc","hakilani","bofjdjkhllb","ocjncleljnecfc","gdonnkodmkejhf","fiflchanfllgnf","kaejakoibgln","hmdlfioacgaci","honmfbcog","mlacbi","gf","ejbbemoeha","acfjegee","lllflaocnnkeadi","mdgoebfgacecmbg","faejgln","kmlmhffgcmekm","akcjmgdg","kmhhh","fdohjehacdln","e","ojba","ohadmod","eaenkdiaokl","dii","cgfjaklblafeifo","imoeflkcgbbem","nbjkmb","jjgm","hofgelg","cnihecmdigdgflg","fnmikkeldjgb","onlhgonldjaedh","fmkdn","kfbcbleen","oejioibnmab","cg","meadghbocjnj","hmmdnkegfeieijn","ijgenomhndlje","maccdcgfjig","iabemie","mlfg","mdblmdaechmeaml","dhlafgjo","eabbiila","kf","oehggehfmijlfmg","klljaejidfhbon","akmbgmignoag","jgbkngmigdfm","kjeelnbn","ajaa","mlcjoiaahoiga","oalnielba","ffmobgkc","kmhoknfffdmo","nagjiffnjhh","dlehllomjok","agaejefhdbk","nnegoijfdj","ndl","dhfginocgi","nflmglgh","bcd","gbgjijemmdio","jk","gidgjbmb","hi","lmgoah","fdebefcech","ach","bahaoj","ccmmblgibgjahi","moid","jhilgedidndm","ldiakemnj","bbnibccm","jkbneoaheaajnm","clkgmbjlgdnl","lobbdldifnnijh","dnmih","jglia","didicmghfe","dlhbcfclf","akbmioocoihkfh","foofdldm","imenimfcame","ifekbmgnbdkc","jjlkaabdollola","gie","hbaj","noomfnfccmgaa","dcjffeg","nb","obdb","lolgjflimkib","eaiigminlakkb","cia","hkf","jknfklaio","igklbiomo","jfjgh","ekgnkfnhjcch","kmonfcclieehlik","oggkmccklnmj","bedhobcl","egmnhajcnhcdgb","imfdhekamfel","bmmkhfdbm","gnjfbcjlecfn","llmkgclm","gafinbnhfe","mlbfedkoeeddfao","kklcdmglleb","ckekmeiea","mi","kfejn","lm","mk","abkoajocfdili","jidac","jonhkanccl","lllodjgnmm","abfeaodlmjkngol","cdncnh","lkcb","abhilnmmhijab","hiljkfakojjld","mbboobkaolkljo","jhkblobaofgoh","ncm","mgbdhmcicomf","oag","akmjdd","abkenodnhj","mljf","afb","afejkobmiffeee","oollnkilabmb","gfaocokmcmjlmb","cokmecdd","bo","endocdnmjiek","bcf","lhllbagiel","bhihgofhj","ffce","neio","ofbfiiab","kjdo","lgfggnamceeo","kofledoinamcj","femhndomndoakoa","fmodaigcka","omakggcalhn","hhhogmcbjnhelkk","mgah","jghjjfmk","ecolelfmcb","eajjkdncafhhgab","obno","fifigfeok","laafjimienff","beckbbmhmofb","nafhihmgnikd","cbcfnhlkne","kao","nlkfhbm","fmh","ohfek","oj","hifgcgi","adhkn","lffgmodeafnn","ngchmhdbmhmhh","mcffimhnlffab","blhmkdhbnhbb","kkb","lgkine","hgfbdbfffanhik","joebhbh","img","kglcddmloo","hoflgfao","bdhgdekb","mggflahnoo","cmnol","imnmmgimmedf","mcjmoofomiia","mlakhbjfnbmgena","ilhmcnkkeg","domhbmkcd","fco","fdio","cmkoagblnd","kmihfigmceiiicm","afgbadbgbaon","menahlemehifooe","jacokdiiokaic","limj","fkedaoomokjbkdi","jkncd","jblmcmfnegnk","jjicjhjhbg","gbfcead","jf","aifnkmnao","effmhlhchngknl","odhjeib","ohcgmgb","bgbd","am","kkjfbdlh","hgbjakkokjgooel","jbeokiakf","flaoba","cifcdnanmk","mice","ihhofdai","ldnfmeiemhf","kefbbohhgineacj","bi","njfie","ociodahlomoekkf","andhoindeca","ajnndjocjeg","bmijkmjbbkgbbh","feanh","bjemcefkfcaenal","edfdenghinm","moal","ndbjdmijh","enccnhmoifa","dbckadjibam","gd","oglj","aldjelhbemle","cmbkofkcoe","ihciacibeh","lcojkclhmibgoif","jfmjncnolfj","gfcmcabhjki","aggfmakaanjb","mhbelld","hon","nkfoikcddehcah","kggbigknacmohb","jbkgndofcmaaohh","gkjano","afhhhh","mjng","jilckm","dekkedjehmenbm","clfm","acmhbkdadgena","oenokachg","lhiea","dceiag","eebgj","oolifidh","dj","cdfn","eghdglgiok","jdhegkefhbdhkm","mhgngafea","akabbcjkdnbc","gcbn","kimdgahf","oc"]    
    
    # s = "fohhemkkaecojceoaejkkoedkofhmohkcjmkggcmnami"
    # fohhemkka
    # wordDict = ["kfomka","hecagbngambii","anobmnikj","c","nnkmfelneemfgcl","ah","bgomgohl","lcbjbg","ebjfoiddndih","hjknoamjbfhckb","eioldlijmmla","nbekmcnakif","fgahmihodolmhbi","gnjfe","hk","b","jbfgm","ecojceoaejkkoed","cemodhmbcmgl","j","gdcnjj","kolaijoicbc","liibjjcini","lmbenj","eklingemgdjncaa","m","hkh","fblb","fk","nnfkfanaga","eldjml","iejn","gbmjfdooeeko","jafogijka","ngnfggojmhclkjd","bfagnfclg","imkeobcdidiifbm","ogeo","gicjog","cjnibenelm","ogoloc","edciifkaff","kbeeg","nebn","jdd","aeojhclmdn","dilbhl","dkk","bgmck","ohgkefkadonafg","labem","fheoglj","gkcanacfjfhogjc","eglkcddd","lelelihakeh","hhjijfiodfi","enehbibnhfjd","gkm","ggj","ag","hhhjogk","lllicdhihn","goakjjnk","lhbn","fhheedadamlnedh","bin","cl","ggjljjjf","fdcdaobhlhgj","nijlf","i","gaemagobjfc","dg","g","jhlelodgeekj","hcimohlni","fdoiohikhacgb","k","doiaigclm","bdfaoncbhfkdbjd","f","jaikbciac","cjgadmfoodmba","molokllh","gfkngeebnggo","lahd","n","ehfngoc","lejfcee","kofhmoh","cgda","de","kljnicikjeh","edomdbibhif","jehdkgmmofihdi","hifcjkloebel","gcghgbemjege","kobhhefbbb","aaikgaolhllhlm","akg","kmmikgkhnn","dnamfhaf","mjhj","ifadcgmgjaa","acnjehgkflgkd","bjj","maihjn","ojakklhl","ign","jhd","kndkhbebgh","amljjfeahcdlfdg","fnboolobch","gcclgcoaojc","kfokbbkllmcd","fec","dljma","noa","cfjie","fohhemkka","bfaldajf","nbk","kmbnjoalnhki","ccieabbnlhbjmj","nmacelialookal","hdlefnbmgklo","bfbblofk","doohocnadd","klmed","e","hkkcmbljlojkghm","jjiadlgf","ogadjhambjikce","bglghjndlk","gackokkbhj","oofohdogb","leiolllnjj","edekdnibja","gjhglilocif","ccfnfjalchc","gl","ihee","cfgccdmecem","mdmcdgjelhgk","laboglchdhbk","ajmiim","cebhalkngloae","hgohednmkahdi","ddiecjnkmgbbei","ajaengmcdlbk","kgg","ndchkjdn","heklaamafiomea","ehg","imelcifnhkae","hcgadilb","elndjcodnhcc","nkjd","gjnfkogkjeobo","eolega","lm","jddfkfbbbhia","cddmfeckheeo","bfnmaalmjdb","fbcg","ko","mojfj","kk","bbljjnnikdhg","l","calbc","mkekn","ejlhdk","hkebdiebecf","emhelbbda","mlba","ckjmih","odfacclfl","lgfjjbgookmnoe","begnkogf","gakojeblk","bfflcmdko","cfdclljcg","ho","fo","acmi","oemknmffgcio","mlkhk","kfhkndmdojhidg","ckfcibmnikn","dgoecamdliaeeoa","ocealkbbec","kbmmihb","ncikad","hi","nccjbnldneijc","hgiccigeehmdl","dlfmjhmioa","kmff","gfhkd","okiamg","ekdbamm","fc","neg","cfmo","ccgahikbbl","khhoc","elbg","cbghbacjbfm","jkagbmfgemjfg","ijceidhhajmja","imibemhdg","ja","idkfd","ndogdkjjkf","fhic","ooajkki","fdnjhh","ba","jdlnidngkfffbmi","jddjfnnjoidcnm","kghljjikbacd","idllbbn","d","mgkajbnjedeiee","fbllleanknmoomb","lom","kofjmmjm","mcdlbglonin","gcnboanh","fggii","fdkbmic","bbiln","cdjcjhonjgiagkb","kooenbeoongcle","cecnlfbaanckdkj","fejlmog","fanekdneoaammb","maojbcegdamn","bcmanmjdeabdo","amloj","adgoej","jh","fhf","cogdljlgek","o","joeiajlioggj","oncal","lbgg","elainnbffk","hbdi","femcanllndoh","ke","hmib","nagfahhljh","ibifdlfeechcbal","knec","oegfcghlgalcnno","abiefmjldmln","mlfglgni","jkofhjeb","ifjbneblfldjel","nahhcimkjhjgb","cdgkbn","nnklfbeecgedie","gmllmjbodhgllc","hogollongjo","fmoinacebll","fkngbganmh","jgdblmhlmfij","fkkdjknahamcfb","aieakdokibj","hddlcdiailhd","iajhmg","jenocgo","embdib","dghbmljjogka","bahcggjgmlf","fb","jldkcfom","mfi","kdkke","odhbl","jin","kcjmkggcmnami","kofig","bid","ohnohi","fcbojdgoaoa","dj","ifkbmbod","dhdedohlghk","nmkeakohicfdjf","ahbifnnoaldgbj","egldeibiinoac","iehfhjjjmil","bmeimi","ombngooicknel","lfdkngobmik","ifjcjkfnmgjcnmi","fmf","aoeaa","an","ffgddcjblehhggo","hijfdcchdilcl","hacbaamkhblnkk","najefebghcbkjfl","hcnnlogjfmmjcma","njgcogemlnohl","ihejh","ej","ofn","ggcklj","omah","hg","obk","giig","cklna","lihaiollfnem","ionlnlhjckf","cfdlijnmgjoebl","dloehimen","acggkacahfhkdne","iecd","gn","odgbnalk","ahfhcd","dghlag","bchfe","dldblmnbifnmlo","cffhbijal","dbddifnojfibha","mhh","cjjol","fed","bhcnf","ciiibbedklnnk","ikniooicmm","ejf","ammeennkcdgbjco","jmhmd","cek","bjbhcmda","kfjmhbf","chjmmnea","ifccifn","naedmco","iohchafbega","kjejfhbco","anlhhhhg"]
    print(wordDict)
    ret = solution.wordBreak(s, wordDict)
    print(ret)
