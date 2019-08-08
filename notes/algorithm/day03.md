#		day03



## 比较器

> 1. **写一个比较器的类**
> 2. **继承Comparator接口，传入参与比较的类对象**
> 3. **重写compare方法**
> 4. **比较返回值**
>    * 返回值是负数  ：  第一个对象应该排在前面
>    * 返回值是正数  ：  第二个对象应该排在前面
>    * 返回值是0      ：    两个对象一样大



**例程：**

```java
//年龄比较器，按照从小到大的顺序排列
public static class AgeAscendingComparator implements Comparator<Student>{


        @Override
        public int compare(Student o1, Student o2) {
            if (o1.age < o2.age){
                return -1;
            }else if (o1.age > o2.age){
                return 1;
            }else {
                return 0;
            }
        }
    }

//这种重写的方式可以写成
		@Override
        public int compare(Student o1, Student o2) {
            return o1.age - o2.age;
        }
```





-----------------





## 桶排序



> **时间复杂度：o(N)**
>
> **额外空间复杂度：o(N)**



**例子：**

**给定一个数组，求如果排序之后，相邻两数的最大差值，要求时
间复杂度O(N)，且要求不能用非基于比较的排序。**

**思路：假设数组中有n个数，设计n+1个桶，按照最小值到最大值的范围进行平均分配，将数组中的数依次放入桶里，但是只记录每个桶的最大值和最小值，根据鸽笼原理，必然会出现一个空桶，然后确定每个桶间最大值与最小值的差值，或者两个相邻的桶之间最大值与最小值之间的差值进行比对**



**解：**

```java
public static int MaxGap(int[] arr){
    
    if(arr == null || arr.length < 2){
        return 0;
    }
    
    
    int len = arr.length;
    int max = Integer.MIN_VALUE;
    int min = Integer.MAX_VALUE;
    
    for(int i = 0;i < len;i++){
        max = Math.max(max,arr[i]);
        min = Math.min(min,arr[i]);
    }
    
    //表明数组中只有一种数
    if(max == min){
        return 0;
    }
    
    //判断最大值和最小值桶是否含有数据
    boolean[] hasNum = new boolean[len + 1];
    int[] maxs = new int[len + 1];
    int[] mins = new int[len + 1];
    
    int bid = 0;
    for(int i = 0;i < len;i++){
        bid = bucket(arr[i],len,max,min);
        //当前值与桶里面的值比较，大的值放在里面
        maxs[bid] = hasNum[bid] ? Math.max(maxs[bid],arr[i]) : arr[i];
        mins[bid] = hasNum[bid] ? Math.min(mins[bid],arr[i]) : arr[i];
        //表明桶里含有数据
        hasNum[bid] = true;
    }
    
    int res = 0;
    int lastMax = maxs[0];
    int i = 1;
    for(;i <= len;i++){
        if(hasNum[i]){
            //下一个桶里面的最小值减去上一个桶里面的最大值与res进行比较
            res = Math.max(res,mins[i] - lastMax);
            lastMax = maxs[i];
        }
    }   
    return res;
}
```



```java
public static int bucket(int[] arr,long len,long max,long min){
    return (int)((num - min) * len / (max - min));
}
```





---------------



## 例题

### 例一

**用数组结构实现大小固定的队列和栈**

**1.用数组实现栈**

```java
public static void StackArray{
    
    private Integer[] arr;
    private Integer index;
    
    //构造方法
    public StackArray(int initSize){
        
        if(initSize < 0){
            throw new IllegalArgumentException("The init size is less than 0 ");
        }
        
    }
    
    //获取栈顶数据
    public Integer peek(){
        
        if(index == 0){
            return null;
        }
        
        return arr[--index];
        
    }
    
    //添加元素
    public void push(int num){
        
        if(index == arr.length){
            throw new ArrayIndexOfBoundsException("The queue is full");
        }
        
        arr[index++] = num;
        
    }
    
    //删除元素
    public Integer pop(){
        if(index == 0){
            throw new ArrayIndexOfBoundsException("The queue is empty");
        }
        
        return arr[--index];
        
    }
    
    
}
```





**用数组实现队列**



```java
public class StackQueue{
    
    private Integer[] arr;
    private Integer size;
    private Integer start;
    private Integer end;
    
    public StackQueue(int initSize){
        if(initSize < 0){
            throw new IllegalArgumentException("The init size less than 0");
        }
        
        arr = new Integer[initSize];
        size = 0;
        start = 0;
        end = 0;
    }
    
    
    public void push(int num){
        if(size == arr.length){
            
            throw new ArrayIndexOfBoundsException("The queue is full");
            
        }
        
        size++;
        arr[end] = num;
        end = end == arr.length - 1 ? 0 : end + 1;
    }
    
    
    public Integer poll(){
        
        if(size == 0){
            throw new ArrayIndexOfBoundsException("The queue is empty");
        }
        
        int tmp = start;
        start = start == arr.length - 1 ? 0 : start + 1;
        return arr[tmp];
    }
    
    
    public Integer peek(){
        if(size == 0){
            return null;
        }
        
        return arr[start];
        
    }
    
    
}
```





-----------------



### 例二

**实现一个特殊的栈，在实现栈的基本功能的基础上，再实现返
回栈中最小元素的操作。
【要求】
1．pop、push、getMin操作的时间复杂度都是O(1)。
2．设计的栈类型可以使用现成的栈结构。**



**思路：设计两个栈，一个栈用于正常的压栈操作，另外一个用于压入最小值，当往第一个栈压入第一个数据的时候也往第二个栈压入，往第一个栈压入第二个数的时候，与第二个栈的栈顶进行比较，大于第二个栈的栈顶时，第二个栈重复压入上一次压入的数据，小于第二个栈栈顶时，就压入当前值。**



```java
public class MyStack2{
    
    private Stack<Integer> stackData;
    private Stack<Integer> stackMin;
    
    public MyStack2(){
        this.stackData = new Stack<Integer>();
        this.stackMin = new Stack<Integer>();
    }
    
    public void push(int num){
        
        if(this.stackMin.isEmpty()){
            this,stackMin.push(num);
        }else if(num < this.getmin()){
            this.stackMin.push(num);
        }else{
            int newMin = this.stackMin.peek();
            this.stackMin.push(newMin);
        }
        this.stackData.push(num);
        
    }
    
   public int pop(){

      	if (this.stackData.isEmpty()){
            throw new ArrayIndexOutOfBoundsException("The stack is empty");
        }

        this.stackMin.pop();
        return this.stackData.pop();

    }
    
    public int getmin(){
        if (this.stackMin.isEmpty()){
            throw new ArrayIndexOutOfBoundsException("The stack is empty");
        }

        return this.stackMin.peek();
        
    }
    
}
```







--------------



### 例三



**如何仅用队列结构实现栈结构？
如何仅用栈结构实现队列结构？**

**用队列实现栈结构**



```java
public class QueueStack{
    
    private Queue<Integer> data;
    private Queue<Integer> help;
    
    public QueueStack(){
        
        data = new LinkedList<Integer>();
        help = new LinkedList<Integer>();
    }
    
    
    public void push(int intNum){
        
        data.add(intNum);
        
    }
    
    
    public int peek(){
        
        if(data.isEmpty()){
            throw new RunTimeException("Stack is empty!");
        }
        
        while(data.size() != 1){
            help.add(data.poll());
        }
        
        int res = data.poll();
        swap();
        return res;
        
    }
    
    
    public int pop(){
        if(data.isEmpty()){
            throw new RunTimeException("Stack is empty!");
        }
        
        while(data.size() > 1){
            help.add(data.poll());
        }
        
        int res = data.poll();
        swap();
        return res;

    }
    
    
    private void swap(){
        
        Queue<Integer> temp = data;
        data = help;
        help = temp;
    }
}
```









-----------



**用栈实现队列结构**



```java
public class TwoStackQueue{
    
    private Stack<Integer> stackPush;
    private Stack<Integer> stackPop;
    
    
    public TwoStackQueue(){
        
        stackPush = new Stack<Integer>();
        stackPop = new Stack<Integer>();
        
    }
    
    //添加
    public void push(int pushNum){
        
        stackPush.push(pushNum);
    }
    
    //获取队列的头
    public int peek(){
        
        if(stackPush.empty && stackPop.empty()){
            
            throw new RunException("The Queue is empty!");
            
        }
        
        dao();
        return stackPop.peek();
        
    }
    
    //删除队列的头
    public int poll(){
        if(stackPush.empty && stackPop.empty()){
            
            throw new RunException("The Queue is empty!");
            
        }
        
        dao();
        return stackPop.pop();
        
        
    }
    
    
    public void dao(){
        
        if(!stackPop.isEmpty()){
            throw new RunException("The Queue is not empty!");
        }
        
        stackPop.push(stackPush.pop());
        
    }
    
    
    
    
    
}
```









