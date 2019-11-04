**Homework #11**  

**1) See Videos for the best models here or in IBMCloud.**  

**2) Changes & Results:**  

- Model parameters changed and observed results (see lunar_lander.py)  
- Training parameters (total iterations and threshold) changed and observed results. (see run_lunar_lander.py). For example, is adam better than adamax?  
  
Try at least three different configurations (one can be the initial "base" configuration) and compare your results. 
The goal is to increase the number of successful landings (noted by the output "Landed it!").


NOTES:  
batch_size = 100
a_candidates = np.random.uniform(low=-1, high=1, size=(batch_size, 2))
s_expanded = np.broadcast_to(new_s, (batch_size, 8))
all_candidates = np.concatenate([s_expanded, a_candidates], axis=1)
r_pred = model.predict(all_candidates)

max_idx = np.argmax(r_pred)
a = a_candidates[max_idx]
