**Homework #11**  

**1) See Videos for the best models here or in IBMCloud.**  

**2) Changes & Results:**  
- Model v1: This is the base model
> Hours: 13  
> Steps: 50,000
> Min Loss: 135  
> Loss Rate: downward slope, potentially not reaching minimum  
> Landings: 31  
> Optimizer: adam  
- Model v2: Optimizer was changed to adamax, everything else was the same  
> Hours: 13  
> Steps: 50,000  
> Min Loss: 168  
> Loss Rate: downward slope, reaching a min loss of 168 (42,000 steps) before increasing to 179  
> Landings: 53  
> Optimizer: adamax  
- Model v3: Optimizer was changed to adadelta, Code speedup was added - see below*, more model layers added - see below^^^.  
> Hours: 13  
> Steps: 50,000O
> Min Loss: 105  
> Loss Rate: downward slope, potentially not reaching minimum  
> Landings: 48  
> Optimizer: adadelta  
- Model v4: Optimizer was changed back to adamax, Code speedup was added - see below*, removed a layr - see below^^^^.  
> Hours: 13  
> Steps: 50,000  
> Min Loss: 135  
> Loss Rate: downward slope, potentially not reaching minimum  
> Landings: 31  
> Optimizer: adamax  

- Model parameters changed and observed results (see lunar_lander.py)  
- Training parameters (total iterations and threshold) changed and observed results. (see run_lunar_lander.py). For example, is adam better than adamax?  
  
Try at least three different configurations (one can be the initial "base" configuration) and compare your results. 
The goal is to increase the number of successful landings (noted by the output "Landed it!").


* Code Speedup:  
batch_size = 100  
a_candidates = np.random.uniform(low=-1, high=1, size=(batch_size, 2))  
s_expanded = np.broadcast_to(new_s, (batch_size, 8))  
all_candidates = np.concatenate([s_expanded, a_candidates], axis=1)  

^^^ v3 New Model:  
Model #3 - Add more 'relu' layers and change optimizer to 'adadelta'  
def nnmodel(input_dim):  
    model = Sequential()  
    model.add(Dense(256, input_dim=input_dim, activation='relu'))  
    model.add(Dense(128, activation='relu'))  
    model.add(Dense(64, activation='relu'))  
    model.add(Dense(32, activation='relu'))  
    model.add(Dense(16, activation='sigmoid'))  
    model.add(Dense(1))  
    model.compile(loss='mean_squared_error', optimizer='adadelta', metrics=['accuracy'])  
    return model  
      
^^^^ v4 New Model:  
Model #4 - removed layers and change optimizer back to 'adamax'  
def nnmodel(input_dim):  
    model = Sequential()  
    model.add(Dense(128, input_dim=input_dim, activation='relu'))  
    model.add(Dense(64, activation='relu'))  
    model.add(Dense(32, activation='relu'))  
    model.add(Dense(16, activation='sigmoid'))  
    model.add(Dense(1))  
    model.compile(loss='mean_squared_error', optimizer='adamax', metrics=['accuracy'])  
    return model  
