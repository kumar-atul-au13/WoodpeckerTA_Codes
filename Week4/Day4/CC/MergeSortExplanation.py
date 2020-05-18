class ColorList:
    color_reg={
        'black':'\u001b[30m',
        'red':'\u001b[31m',
        'green':'\u001b[32m',
        'yellow':'\u001b[33m',
        'blue':'\u001b[34m',
        'magenta':'\u001b[35m',
        'cyan':'\u001b[36m',
        'white':'\u001b[37m',
        'bgBlack':'\u001b[40m',
        'bgRed':'\u001b[41m',
        'bgGreen':'\u001b[42m',
        'bYellow':'\u001b[43m',
        'bBlue':'\u001b[44m',
        'bgMagenta':'\u001b[45m',
        'bCyan':'\u001b[46m',
        'bbgWhite':'\u001b[47m',
        'reset':'\u001b[0m',
    }

    def __init__(self,lst,seg_name_colors={},set_prev_space=0):
        self.set_list(lst)
        self.set_prev_space(set_prev_space)
        self.set_max_digit()
        self.set_seg_name_col(seg_name_colors)
        self.reset='\u001b[0m'


    def set_seg_name_col(self,segment_name_color={}):
        for seg in segment_name_color:
            if segment_name_color[seg] in ColorList.color_reg:
                ColorList.color_reg[seg]=segment_name_color[seg]
    def set_prev_space(self,prev_space):
        self.prev_space=prev_space
    def set_list(self,lst):
        self.lst=lst
    def set_max_digit(self):
        self.max_digit= max(map(lambda x:len(str(x)),self.lst))
    def set_seg_indexes(self,tup_lst,space_tup_lst=None,space_clr=None):
        final_ans=" ".join([" "]*self.prev_space)
        if len(final_ans)>0:
            final_ans+=" "
        res_begin,res_end=self.build_start_end_dict(tup_lst)
        space_beg,space_end=self.build_start_end_SPACE_dict(space_tup_lst)
        isTextColor=False
        TextColor=None
        isSpaceColor=False
        for indx,elem in enumerate(self.lst):
            if indx in res_begin:
                isTextColor=True
                TextColor=res_begin[indx]
            if isTextColor:
                final_ans+=TextColor
            final_ans+=str(elem).rjust(self.max_digit)
            if indx in res_end:
                isTextColor=False
            final_ans+=ColorList.color_reg['reset']


            if indx in space_beg:
                isSpaceColor=True
            if indx in space_end:
                isSpaceColor=False
            if isSpaceColor and space_clr:
                final_ans+=ColorList.color_reg[space_clr]
            final_ans+=' '
            if isSpaceColor and space_clr:
                final_ans+=ColorList.color_reg['reset']

        return final_ans


    def build_start_end_dict(self,tup_list):
        if tup_list is None or len(tup_list)==0:
            return {},set()
        res_begin={}
        res_end=set()
        for tup in tup_list:
            if tup[1]>tup[2]:
                continue
            res_begin[tup[1]]=ColorList.color_reg[tup[0]]
            res_end.add(tup[2])
        return res_begin,res_end

    def build_start_end_SPACE_dict(self,tup_list):
        if tup_list is None or len(tup_list)==0:
            return set(),set()
        space_beg=set()
        space_end=set()
        for tup in tup_list:
            if tup[0]>tup[1]:
                continue
            space_beg.add(tup[0])
            space_end.add(tup[1])
        return space_beg,space_end
# print(clr_test)
def merge(arr,brr):
    lena=len(arr)
    lenb=len(brr)
    res=[]
    ia,ib=0,0

    while ia<lena and ib<lenb:
        if arr[ia]<brr[ib]:
            res.append(arr[ia])
            ia+=1
        else:
            res.append(brr[ib])
            ib+=1

    for i in range(ia,lena):
        res.append(arr[i])
    for i in range(ib,lenb):
        res.append(brr[i])
    # print(res,arr,brr)
    return res
def merge_itter(arr):
    print(ColorList(arr).set_seg_indexes([('bgMagenta',0,len(arr)-1)]))
    print()
    i=1
    while i<=len(arr):
        for j in range(0,len(arr),2*i):
            arr[j:j+2*i]=merge(arr[j:j+i],arr[j+i:j+2*i])
            print(ColorList(arr[j:j+2*i]).set_seg_indexes([('bgMagenta',0,2*i-1)],[(0,2*i-1)],'bgMagenta'),end="")
        i*=2
        print()
        print()
arr=list(range(99,10,-2))
print(*arr)
merge_itter(arr)
print(*arr)



