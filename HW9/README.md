**Questions**

**Q1)** Please submit the nohup.out file along with screenshots of your Tensorboard indicating training progress (Bleu score, eval loss) over time.
> See nohup.out  
> Bleu_and_Eval_Loss.JPG, globalstep_learningrate_trainloss.JPG images  

**Q2)** How long does it take to complete the training run? (hint: this session is on distributed training, so it will take a while)  
> ~13 hours  

**Q3)** Do you think your model is fully trained? How can you tell?  
> No. The rates are still changing slowly (BLEU increasing, Eval Loss & Learning Rate decreasing). I would expect more of a flatline.  

**Q4)** Were you overfitting?  
> In the beginning it was overfitting, after 50k I don't see this as much. (train loss and eval loss were matched)  

**Q5)** Were your GPUs fully utilized?  
> See GPU_Util.jpg  
> Yes! Nvidia-smi shows a GPU utilization at 100%  

**Q6)** Did you monitor network traffic (hint: apt install nmon ) ? Was network the bottleneck?  
> See NMon.jpg  
> I assume the network traffic is the bottleneck since the CPU/GPU would be much faster.  

**Q7)** Take a look at the plot of the learning rate and then check the config file. Can you explan this setting?  
> warmup_steps was 8000, which matches the 'warmup' period that is displayed in the learning_rate graph.  

**Q8)** How big was your training set (mb)? How many training lines did it contain?  
> 909MB  
> -rw-r--r-- 1 root root  909M Oct 22 19:32 train.clean.en.shuffled.BPE.32K.tok  

**Q9)** What are the files that a TF checkpoint is comprised of?  
> data, index, metafile  
-rw-r--r-- 1 root root 813M Oct 22 19:48 model.ckpt-0.data-00000-of-00001  
-rw-r--r-- 1 root root   1M Oct 22 19:48 model.ckpt-0.index  
-rw-r--r-- 1 root root  16M Oct 22 19:48 model.ckpt-0.meta  

**Q10)** How big is your resulting model checkpoint (mb)?  
> ~830MB  

**Q11)** Remember the definition of a "step". How long did an average step take?  
> ~.76s  

**Q12)** How does that correlate with the observed network utilization between nodes?  
> 860MB for model size  
> 23hrs = 82,800 seconds  
> Network Traffic = 1,000,000 Bytes/second
> This results in 828,000,000,000 Bytes or 828MB  so this is pretty close to 860MB  

