# this scripts compute the accuracy from the result generated with shownet.py --show-preds=probs --save-preds='some path' --multiview-test=1
import numpy as n
import sys, os, glob, cPickle

def multiview_test(file_name, num_view=10, method=0, top_n=5):
    preds=cPickle.load(open(file_name, 'rb'))
    # the preds are interlaced: img1_view1, img2_view1,...,imgn_view2,img1_view2,img2_view2,...,imgn_view2,...,img1_viewk, img2_viewk,...,imgn_viewk
    num_data=preds.shape[0]/num_view
    num_class=preds.shape[1]
    preds=n.reshape(preds, (num_view, num_data, num_class))
    gt=preds[:,:,0]
    data=preds[:,:,1:]
    num_acc=0
    if method==0:
        # method 0, we use probablity to accumulate view
        prob=1-n.prod(1-data, axis=0)
    else:
        # method 1, pick the max view
        prob=n.max(data, axis=0)
    # the sort is in ascending order
    thresh=n.sort(prob, axis=1)
    thresh=thresh[:,thresh.shape[1]-top_n]
    for i in range(thresh.shape[0]):
        if (prob[i,gt[0,i]]>=thresh[i]):
            num_acc=num_acc+1
    print num_data, 'processed and found', num_acc, 'corrected instances'
    return num_data,num_acc
    
if __name__=="__main__":
    argn=len(sys.argv)
    if argn<2:
        print "usage: python testnet.py root_dir [num_view] [method] [top_n]"
    root_dir=sys.argv[1]
    if argn<3:
        num_view=10
    else:
        num_view=int(sys.argv[2])
    if argn<4:
        method=0
    else:
        method=int(sys.argv[3])
    if argn<5:
        top_n=10
    else:
        top_n=int(sys.argv[4])
    print "current usage: python testnet.py", sys.argv[1], num_view, method, top_n

    old_dir=os.getcwd()
    os.chdir(root_dir)
    pred_list=glob.glob('predictions_batch_*')
    print pred_list
    num_data=0
    num_acc=0
    for i in pred_list:
        batch_data,batch_acc=multiview_test(i, num_view, method, top_n)
        num_data=num_data+batch_data
        num_acc=num_acc+batch_acc
    print "accuracy is", 1.0*num_acc/num_data, "-", num_acc, "/", num_data
    os.chdir(old_dir)
