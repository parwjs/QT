

#	笔记一

##	冒泡排序算法

**思路一：从前往后式**

```java
public static void bubbleSort(int[] arr){
	for(int i=0;i<arr.length;i++){
		for(int j=i+1;j<arr.length-1-i;j++){
			if(arr[i] > arr[j]){
				swap(arr,i,j);
			}
		}
	}
	
	for(int i:arr){
		System.out.print(i + " ");
	}
	System.out.println();
}
```



-------------------------



**思路二：从后往前式**

```
public static void bubbleSort(int[] arr){
	for(int end=arr.leng-1;end>0;end--){
		for (int i = 0; i < end;i++){
                if (arr[i] > arr[i+1]){
                    swap(arr,i,i+1);
                }
            }
	}
	
	for(int i:arr){
		System.out.print(i + " ");
	}
	System.out.println();
}
```



**复杂度：o(n²)**



--------------

##	选择排序算法

```java
public static void SelectionSort(int[] arr){

	for(int i=0;i<arr.length-1;i++){
		int minIndex = i;
		for(int j=i+1;j<arr.length;j++){
			minIndex = arr[j] < arr[minIndex]?j:minIndex;
		}
		swap(arr,i,minIndex);
	}

}
```





--------------------

##	插入排序算法

```java
 public static void InsertionSort(int[] arr){
 	for(int i = 1;i < arr.length;i++){
 		for(int j = i - 1;j >= 0 && arr[j] > arr[j+1];j--){
 			swap(arr,j,j+1);
 		}
 	}
 
 	  for (int i:
                arr) {

            System.out.print(i+" ");
        }
        System.out.println();
 
 }
```



**复杂度：根据数据情况**

**最好情况：数组已经有序：o(n)**

**最坏情况：数组倒序：o(n²)**



------------------------



##	对数器

> 	1.	**生成长度随机的数组**
>
> ```java
> public static int[] generateRandomArray(int size,int value){
> 
> 	int[] arr = new int[(int)(size + 1) * Math.random()];
> 	for(int i = 0;i < arr.length;i++){
> 		arr[i] = (int)((value + 1) * Math.random() - value * Math.random());
> 	}
> 	return arr;
> 
> }
> ```
>
> 2. **复制数组**
>
> ```java
> public static int[] copyArray(int[] arr){
> 	
> 	if(arr == null){
> 		return;
> 	}
> 	int[] res = new int[arr.length];
> 	for(int i = 0;i < arr.length;i++){
> 		res[i] = arr[i];
> 	}
> 	
> 	return res;
> 
> }
> ```
>
> 3. **写一个绝对正确的方法，不要在意复杂度**
>
> ```java
> public static void rightMethod(int[] arr){
> 	Arrays.sort(arr);
> }
> ```
>
> 4. **比对方法**
>
> ```java
> public static boolean isEqual(int[] arr1,int[] arr2){
> 	
> 	if((arr1 == null && arr2 != null) || (arr1 != null && arr2 == null)){
> 		return false;
> 	}
> 	
> 	if(arr1 == null && arr2 == null){
> 		return true;
> 	}
> 	
> 	if(arr1.length != arr2.length){
> 		return false;
> 	}
> 	
> 	for(int i = 0;i < arr1.length;i++){
> 		if(arr1[i] != arr2[i]){
> 			return false;
> 		}
> 	}
> 	
> 	return true;
> 	
> }
> ```
>
> 5. **打印数组**
>
> ```
> public static void printArray(int[] arr){
> 
> 	if(arr == null){
> 		return;
> 	}
> 	for(int i = 0;i < arr.length;i++){
> 		System.out.print(arr[i] + " ");
> 	}
> 	
> 	System.out.println();
> 
> }
> ```
>
> 



6. **对数器的使用**

```
//for test
public static void main(String[] args){
	int testTime = 500000;
	int size = 10;
	int value = 100;
	boolean succeed = true;
	for(int i = 0;i < testTime;i++){
		int[] arr1 = generateRandomArray(size,value);
		int[] arr2 = copyArray(arr1);
		int[] arr3  = copyArray(arr3);
		bubbleSort2(arr1);
		rightMethod(arr2);
		if(!isEqual(arr1,arr2)){
			succeed = false;
			printArray(arr3);
			break;
		}
	}
	
	int[] arr = generateRandomArray(size,value);
	printArray(arr);
	bubbleSort2(arr);
	printArray(arr);

}
```





-----------------------



##	master公式的使用

**T(N) = a*T(N/b) + o(N^d)**



**1) 	log(b,a) > d  -> 复杂度为o(N^log(b,a))**

**2)	log(b,a) = d  ->复杂度为o(N^d * logN)**

**3)	log(b,a) < d  ->复杂度为o(N^d)**



**a表示执行的次数**



------------

##	递归

**递归例子：**

```java
public static int getMax(int[] arr,int L,int R){

        if (L == R){
            return arr[L];
        }

        int mid = (L + R) / 2;
        int maxL = getMax(arr,0,mid);
        int maxR = getMax(arr,mid + 1,R);

        return Math.max(maxL,maxR);

    }
```





----------------



##	归并排序

**时间复杂度：o(N*logN)，额外空间复杂度：o(N)**

**思路：**

**将数组分成两部分，并且将左右两部分分别排好序，然后有两个指针指向左右两边的第一个值，比较大小，小的值填入数组，然后指针后移，直到某一边走完，将剩下的数直接拷贝到数组**



```java
public static void mergeSort(int[] arr){
	
	if(arr == null || arr.length < 2){
		return;
	}
	
	sortProcess(arr,0,arr.length - 1);

}
```



```java
public static void SortProcess(int[] arr,int L,int R){

	if(L == R){
		return;
	}
	
	int mid = L + ((R - L) >> 1);
	SortProcess(arr,L,mid);
	SortProcess(arr,mid+1,R);
	mergeSort(arr,L,mid,R);
	

}
```



```
public static void mergeSort(int[] arr,int L,int mid,int R){

	int[] hellp = new int[R - L + 1];
	int i = 0;
	int p1 = L;
	int p2 = mid + 1;
	
	while(p1 <= mid && p2 <= R){
		
		help[i++] = arr[p1] < arr[p2] ? arr[p1++] : arr[p2++];
	}
	
	while(p1 <= mid){
		help[i++] = arr[p1++];
	}
	
	while(p2 <= R){
		help[i++] = arr[p2++];
	}
	
	for(int j = 0;j < help.length;j++){
		
		arr[L + j] = help[j];
	
	}

}
```

---------------

**小和问题和逆序对问题
小和问题
在一个数组中，每一个数左边比当前数小的数累加起来，叫做这个数组的小和。求一个数组
的小和。
例子：
[1,3,4,2,5]
1左边比1小的数，没有；
3左边比3小的数，1；
4左边比4小的数，1、3；
2左边比2小的数，1；
5左边比5小的数，1、3、4、2；
所以小和为1+1+3+1+1+3+4+2=16
逆序对问题
在一个数组中，左边的数如果比右边的数大，则折两个数构成一个逆序对，请打印所有逆序
对。**



```java
public static int SmallSum(int[] arr){

        if (arr == null || arr.length < 2){
            return 0;
        }


      return   mergeSort(arr,0,arr.length - 1);

    }
```



```java
public static int mergeSort(int[] arr,int L,int R){

        if (L == R){
            return 0;
        }

        int mid = L + ((R - L) >> 1);

        return mergeSort(arr,L,mid) + mergeSort(arr,mid + 1,R) + merge(arr,L,mid,R);


    }
```



```java
public static int merge(int[] arr,int L,int mid,int R){

        int[] help = new int[R - L + 1];
        int i = 0;
        int res = 0;
        int p1 = L;
        int p2 = mid + 1;

        while (p1 <= mid && p2 <= R){

            res += arr[p1] < arr[p2] ? arr[p1] * (R - p2 + 1) : 0;
            help[i++] = arr[p1] < arr[p2] ? arr[p1++] : arr[p2++];

        }


        while (p1 <= mid){

            help[i++] = arr[p1++];

        }

        while (p2 <= R){

            help[i++] = arr[p2++];
        }

        for (int j = 0; j < help.length; j++) {

            arr[L + j] = help[j];

        }

        return res;


    }
```

