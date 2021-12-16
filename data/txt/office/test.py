pred = open('labeled_source_images_dslr_amazon_1_10_pseudo.txt','r').readlines()
gt = open('labeled_source_images_amazon.txt','r').readlines()
length = len(pred)
cnt=0.
for i in range(length):
    if pred[i]==gt[i]:
        cnt=cnt +1
print('Acc no eval:',cnt/length)
#the above is no eval
#the follows is open eval
pred = open('labeled_source_images_dslr_amazon_2_10_pseudo.txt','r').readlines()
gt = open('labeled_source_images_amazon.txt','r').readlines()
length = len(pred)
cnt=0.
for i in range(length):
    if pred[i]==gt[i]:
        cnt=cnt +1
print('Acc open eval:',cnt/length)
