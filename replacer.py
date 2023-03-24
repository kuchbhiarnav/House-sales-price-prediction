def replacer(A):
    import pandas as pd
    Q=pd.DataFrame(A.isna().sum(),columns=["Ct"])
    missing_cols=list= (Q[Q.Ct>0].index)
    for i in missing_cols:
        if(A[i].dtypes == "object"):
            x= (A[i].mode())[0]
            A[i]= A[i].fillna(x)
        else:
            y= A[i].mean()
            A[i]= A[i].fillna(y)
            

def outliers(A):
    T=[]#stores index value
    for i in range(0,len(A.columns)):#rows
        for j in range(0,A.shape[0]):#columns
            x=A.iloc[j,i]
            if(x>3 or x<-3):
                T.append(j)
                
    from numpy import unique
    rows_to_del=list(unique(T))
    return rows_to_del