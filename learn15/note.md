一: 异步IO
	a.多线程和多进程的模型虽然解决了并发问题，但是系统不能无上限地增加线程
	b.CPU高速执行能力和IO设备的龟速严重不匹配
二：协程
	a.协程，又称微线程，纤程。英文名Coroutine。
	b.子程序调用是通过栈实现的，一个线程就是执行一个子程序
	c.协程看上去也是子程序，但执行过程中，在子程序内部可中断，
	  然后转而执行别的子程序，在适当的时候再返回来接着执行
	优势：
		a.最大的优势就是协程极高的执行效率。
		  没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显
		b.不需要多线程的锁机制
	实现：
		a.通过generator实现的
		b.通过for循环来迭代，
		  还可以不断调用next()函数获取由yield语句返回的下一个值
	note: yield不但可以返回一个值，它还可以接收调用者发出的参数。
		  
	协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产，效率极高

	总结：
	asyncio提供了完善的异步IO支持；

	异步操作需要在coroutine中通过yield from完成；

	多个coroutine可以封装成一组Task然后并发执行。