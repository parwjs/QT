

# 一、SpringBoot入门

## 1、SoringBoot简介

> 简化Spring应用开发的一个框架
>
> 整个Spring技术栈的一个大整合
>
> J2EE开发的一站式解决方案

### 优点：

+ 快速创建独立运行的Spring项目以及与主流框架集成
+ 使用嵌入式的Servlet容器，应用无需打成WAR包
+ starters自动依赖与版本控制
+ 大量的自动配置，简化开发，也可修改默认值
+ 无需配置XML，无代码生成，开箱即用
+ 准生产环境的运行时应用监控
+ 与云计算的天然集成



## 2、微服务

2014年，martin fowler

微服务：架构风格

一个应用应该是一组小型服务；可以通过HTTP的方式进行互通；



每一个更能元素最终都是一个可独立替换和独立升级的软件单元；

## 3、SpringBoot HelloWorld

一个功能

浏览器发送hello请求，服务器接受请求并处理，响应Hello World字符串;

###  1、创建一个SpringBoot工程

### 导入依赖

```java
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>1.5.9.RELEASE</version>
    </parent>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
    </dependencies>
```



### 3、编写一个主程序；启动SpringBoot应用

```java
/** @SpringBootApplication来标注一个主程序类，说明这是一个SpringBoot应用 */
@SpringBootApplication
public class HelloWorldMainApplication {

    public static void main(String[] args) {
        //Spring应用启动起来
        SpringApplication.run(HelloWorldMainApplication.class,args);
    }
}
```

### 4、编写相关的Controller、Service

```java
@Controller
public class HelloController {

    @ResponseBody
    @RequestMapping("/hello")
    public String hello() {

        return "HelloWorld!";

    }
}
```



### 5、运行主程序测试

### 6、简化部署

```java
    <!-- 这个插件，可以将应用打包成一个可执行的jar包 -->
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
```

![Maven打包](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1570773650826.png)

**先导入上面的jar包，然后使用Maven的打包功能，打包完成后直接使用java -jar命令执行**



## 4、HelloWorld探究

### 1、POM文件

```java
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>1.5.9.RELEASE</version>
    </parent>
    它的父项目是
    	<parent>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-dependencies</artifactId>
		<version>1.5.9.RELEASE</version>
		<relativePath>../../spring-boot-dependencies</relativePath>
	</parent>
	他是来真正管理SpringBoot应用里面的所有依赖版本;

```

**SpringBoot版本仲裁中心**

以后导入依赖默认不需要写版本;(没有在dependencies里面管理的依赖自然需要声明版本号)

#### 1、父项目

```java
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
```

#### 2、启动器

**spring-boot-starter**-web

​		spring-boot-starter：spring-boot场景启动器;帮我们导入了web模块正常运行所依赖的组件



SpringBoot将所有的功能场景都抽取出来，做成一个个的starters(启动器),只需要在项目里面引入这些starters相关场景的依赖都会导入进来。要用什么功能就导入什么场景的启动器

### 2、主程序类、主入口类

```java
@SpringBootApplication
public class HelloWorldMainApplication {

    public static void main(String[] args) {
        //Spring应用启动起来
        SpringApplication.run(HelloWorldMainApplication.class,args);
    }
}
```

@SpringBootApplication：SpringBoot应用标注在某个类上说明这个类是SpringBoot的主配置类，SpringBoot就应该运行这个类的main方法来启动SpringBoot应用

```java
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Inherited
@SpringBootConfiguration
@EnableAutoConfiguration
@ComponentScan(excludeFilters = {
		@Filter(type = FilterType.CUSTOM, classes = TypeExcludeFilter.class),
		@Filter(type = FilterType.CUSTOM, classes = AutoConfigurationExcludeFilter.class) })
public @interface SpringBootApplication {
```



@**SpringBootConfiguration**：SpringBoot的配置类

​		标注在某个类上，表示这是一个SpringBoot的配置类；

​		@**Configuration**：配置类上来标注这个注解；

​				配置类 --- 配置文件；配置类也是容器中的一个组件；@Component



@**EnableAutoConfiguration**：开启自动配置功能；

​			以前需要配置的东西，SpringBoot帮我们自动配置；											@**EnableAutoConfiguration**告诉SpringBoot开启自动配置的功能，这样自动配置才能生效；

```java
@AutoConfigurationPackage
@Import(EnableAutoConfigurationImportSelector.class)
public @interface EnableAutoConfiguration {
```

@**AutoConfigurationPackage**：自动配置包

​		@**Import**(AutoConfigurationPackages.Registrar.class)：

​		Spring的底层注解@Import,给容器中导入一个组件；导入的组件由AutoConfigurationPackages.Registrar.class；

==将主配置类(@SpringBootApplication标注的类)的所在包及下面所有子包的所有组件扫描到Spring容器中；==

​		@Import(EnableAutoConfigurationImportSelector.class)；

​				给容器中导入组件？

​				EnableAutoConfigurationImportSelector：导入哪些组件的选择器；

​				将所有需要导入的组件以全类名的方式放回；这些组件都会被添加到容器中；	

会给容器中导入非常多的自动配置类(xxxAutoConfiguration);就是给容器中导入这个场景需要的所有组件，并配置好这些组件；

![自动配置类](images\Import的自动导入组件.jpg)

​				

有了自动配置类，免去了手动编写配置注入功能组件等的工作;


SpringFactoriesLoader.loadFactoryNames(EnableAutoConfiguration.class,classLoader);

==SpringBoot在启动的时候从类路径下的META-INF/spring.factories中获取EnableAutoConfiguration指定的值，将这些值作为自动配置类导入到容器中，自动配置类就生效，帮我们进行自动配置工作；==以前需要自己配置的东西，自动配置类都帮我们；

J2EE的整体整合方案和自动配置都在spring-boot-autoconfigure-1.5.9.RELEASE.jar;



---

## 5、使用Spring Initializer快速创建SpringBoot项目

默认生成的SpringBoot项目；

+ 主程序已经生成好了，我们只需要我们自己的逻辑
+ resources文件夹中目录结构
  + static：保存所有得到静态资源；jss css images；
  + templates：保存所有的模板页面；(SpringBoot默认jar包使用嵌入式的Tomcat，默认不支持JSP页面)；可以使用模板引擎(freemarker、thymeleaf)；
  + application.properties：SpringBoot应用的配置文件；可以修改一些默认设置；



# 二、配置文件

## 1、配置文件

SpringBoot使用一个全局的配置文件，配置文件名是固定的；

+ application.properties
+ application.yml

配置文件的作用：修改SpringBoot自动配置的默认值;SpringBoot在底层都给我们配置好；

YAML(YAML Ain't Markup Language)

​		YAML A Markup Language：是一个标记语言

​		YAML isn't Markup Language：不是一个标记语言

标记语言：

​		以前的配置文件；大多使用的是xxxx.xml文件；

​		YAML：以数据为中心，比json、xml等更适合做配置文件；

​		YAML：配置例子

```java 
server:
  port: 8081
```

​		Properties配置例子

```java
server.port=8081
```

​		XML配置例子

```java
<server>
	<port>8081</port>
<server>
```



## 2、YAML语法：

### 1、基本语法

k:(空格)v：表示一对键值对(空格必须有)；

以**空格**的缩进来控制层级关系；只要是左对齐的一列数据，都是同一个层级的

```java
server:
	port: 8081
    path: /hello
```

属性和值也是大小写敏感;





### 2、值的语法

### 字面量：普通的值(数字、字符串、布尔)

​		k：v：字面直接来写；

​				字符串默认不用加上单引号或者双引号；

​				"":双引号；不会转义字符串里面的特殊字符；特殊字符会作为本身想表示的例子

​						name："zhangsan \n list":输出；张三 换行 list

​				'':单引号;会转义特殊字符，特殊字符最终只是一个普通的字符串数据

​						name："zhangsan \n list":输出；zhangsan \n list



### 对象、Map(属性和值)(键值对)：

​		k​：v：在下一行写对象的属性和值的关系；注意缩进

​				对象还是k:v的方式

```yml
friends:

​		 lastName:zhangsan

​	      age:20
```

​			行内写法：

```yml
friends: {lastName: zhangsan,age: 18}
```

数组(List、Set)：

​	用-值表示数组中的一个元素

```yml
pets:
 - cat
 - dog
 - pig
```

行内写法

```yml
pets: [cat,dog,pig]
```



### 3、配置文件注入

配置文件

```yml
person:
  lastName: zhangsan
  age: 18
  boss: false
  birth: 2017/12/12
  maps: {k1: v1,k2: v2}
  lists:
    - lisi
    - zhaoliu
  dog:
    name: 小狗
    age: 2
```

JavaBean:

```yml
/**
 * 将配置文件中配置的每一个属性的值，映射到这个组件中
 * @ConfigurationProperties：告诉SpringBoot将本类中的所有属性和配置文件中相关的配置进行绑定；
 *      prefix = "person" ： 配置文件中哪个下面的属性进行一一映射
 *
 * 只有这个组件是容器中的组件，才能容器提供的@ConfigurationProperties功能；
 */
@Component
@ConfigurationProperties(prefix = "person")
public class Person {

    private String lastName;
    private Integer age;
    private boolean boss;
    private Date birth;


    private Map<String,Object> maps;
    private List<Object> lists;
    private Dog dog;
```



可以导入配置文件处理器，以后编写配置就有提示了

```xml
        <!-- 导入配置文件处理器，配置文件进行绑定就会有提示 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-configuration-processor</artifactId>
            <optional>true</optional>
        </dependency>
```

