#	day02

##	荷兰国旗问题

**给定一个数组arr，和一个数num，请把小于num的数放在数组的
左边，等于num的数放在数组的中间，大于num的数放在数组的
右边。
要求额外空间复杂度O(1)，时间复杂度O(N)**



```java
public static int[] partition(int[] arr,int L,int R,int num){
    
    int less = L - 1;
    int more = R + 1;
    //将L当作向前移动的指针cur
    while(L < more){
        if(arr[L] < num){
            swap(arr,++less,L);
        }
        //L指针停着不动，继续等待判断
        //多个 if    每个if都执行
        //else if  如果前面的有一个成立  那么后面的都不执行
        else if(arr[L] > num){
            swap(arr,--more,L);
        }
        else{
            L++;
        }
    }
    return new int[]{less + 1,more - 1};
    
}
```





---------------



##	随机快速排序算



**思路：从数组中随机选择一个数，并将它和最右边的数换位置，将大于这个数的放右边，小于这个数的放左边，等于这个数的放中间，最后让这个数和等于这个数的下一个指针所指的数交换位置，让其回到等于这个数的区域**



**可以用荷兰国旗问题来改进快速排序**

**时间复杂度o(N*logN)，额外空间复杂度o(logN)**





```java
public static void quickSort(int[] arr,int L,int R){
    
    if(arr == null || arr.length < 2){
        return;
    }
    
   if(L < R){
       
       //随机选择最右的数
       swap(arr,L + (int)(Math.random() * (R - L + 1)),R);
       
       int[] p = partition(arr,L,R);
       quickSort(arr,L,p[0] - 1);
       quickSort(arr,p[1] + 1,R);
   }
    
}
```



```java
public static int[] partition(int[] arr,int L,int R){
    
    int less = L - 1;
    int more = R;
    
    while(L < more){
        
        if(arr[L] < arr[R]){
            swap(arr,++less,L++)
        }
        else if(arr[L] > arr[R]){
            swap(arr,--more,L);
        }
        else{
            L++;
        }
        
        swap(arr,more,R);
        
        return new int[]{less + 1, more};
        
    }
    
}
```



-------------------



##	堆排序



**时间复杂度o(N*logN)，额外空间复杂度o(1)**

**堆就是完全二叉树**

> **大根堆**：**在完全二叉树中任何一颗子树的最大值都是这棵子树的头部所形成的结构**
>
> **小根堆**：**在完全二叉树中任何一颗子树的最小值都是这棵子树的头部所形成的结构**





**将数组变成大根堆：**

**每个子节点和父节点进行比较，比父节点大就换位置**

**代价：**

​		**每次加进来一个数，设数的下标为i，都要与i-1个数进行调整，由于只和父节点进行比较调整，所以调整代价为log(i-1)，每个数都是这样，所以调整代价为(log1+log2+...+logN) -> o(N)**



**所以建立一个大根堆的复杂度为o(N)**



```java
public static void heapSort(int[] arr){
    
    if(arr == null || arr.length < 2){
        return;
    }
 
    for(int i = 0;i < arr.length;i++){
        //形成大根堆
        heapInsert(arr,i);
    }
    
    int heapSize = arr.length;
    //将大根堆堆顶的值与堆最后一个叶节点进行交换
    swap(arr,0,--heapSize);
    
    while(heapSize > 0){
        
        //重新形成大根堆，将交换后的堆顶往下沉
        heapify(arr,0,heapSize);
        //再次交换
        swap(arr,0,--heapSize)
        
    }
}
```





```java
//插入一个值，形成大根堆
public static void heapInsert(int[] arr,int index){
    
    while(arr[index] > arr[(index - 1) / 2]){
        
        swap(arr,inde,(index - 1) / 2);
        index = (index - 1 ) / 2;
        
    }
       
}
```



```java
//值变小，往下沉的操作
public static void heapify(int[] arr,int index,int heapSize){
    
	int left = index * 2 + 1;
    //heapSize标志这个大根堆的界限
    while(left < heapSize){
        
        //得出左右孩子中较大的下标
        int largest = left + 1 < heapSize && arr[left + 1] > arr[left] ? left + 1 : left;
        //将左右孩子中的最大值和当前值进行比较，如果比当前值大，largest就是左右孩子中最大值的下标，否则就是当前值的下标
        largest = arr[largest] > arr[index] ? largest : index;
        
        //如果说largest是当前值的下标，就说明当前值最大，不需要换位置，直接跳出循环
        if(largest == index){
            break;
        }
    
        swap(arr,index,largest);
    	index = largest;
    	left = index * 2 + 1;
    
    }
    
    
}
```

 



------------------



## 排序的稳定性



**相同的值在原始序列中相对位置不发生改变**

**排序之后不打乱在原始序列中的相对位置**

**可以实现稳定性的算法：**

> 	1.	**冒泡排序**
>  	2.	**插入排序**



**在数据量较小的时候为什么会使用快排(复杂度很高的排序算法)?**

​	**答：数据量较低时，指标都是差不多的，但是快排(复杂度很高的排序算法)常数项低**



**为什么自己定义的类型使用归并排序?**

**从稳定性出发，保存一些信息。**



> ​	奇数放数组左边，偶数放数组右边，而且顺序不发生改变，其实是不可能的。。。
>
> ​	额外空间复杂度o(1)
>
> ​	时间复杂度o(N)











