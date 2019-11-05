**Homework #11**  
  
**1) The 5 different model videos are included (v1 to v5) and in IBMCloud (https://s3.sjc04.cloud-object-storage.appdomain.cloud/w251-hw11/).  Python code is attached to show the code changes.**  
  
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
> Hours: 7  
> Steps: 50,000O  
> Min Loss: 105  
> Loss Rate: downward slope, potentially not reaching minimum  
> Landings: 48  
> Optimizer: adadelta  
- Model v4: Optimizer was changed back to adamax, Code speedup was added - see below*, removed a layer - see below^^^^.  
> Hours: 7  
> Steps: 50,000  
> Min Loss: 105  
> Loss Rate: downward slope, potentially not reaching minimum  
> Landings: 35  
> Optimizer: adamax  
  
- Model v5: Same as Model 4, except training time was increased from 3,000 to 10,000  
> Hours: 6  
> Steps: 50,000  
> Min Loss: 121  
> Loss Rate: downward slope, potentially not reaching minimum  
> Landings: 47  
> Optimizer: adamax  

Adamax is a special case of Adam where its second-order moment v0 is replaced by infinite-order moment which makes the algorithm more stable and more robust to noise in the gradients.  In this exercise the number of landings almost doubled (31 to 53) moving from adam to adamax.  
  
Adadelta is an extension of Adagrad that restricts the window of accumulated past gradients to a fixed size, w.  The number of landings were similar to Adamax (48 to 53), though the minimum loss was lower at 105 after 50,000 steps.
  
The Model layers were increased for Models 3 and 4, which seemed to have little impact on the number of landings. In model 4, Adamax was used again with more layers relative to Model 2, which resulted in landing decreasing from 53 (model 2) to 35 (model 4)
  
By increasing the training from 3,000 to 10,000, there was an increase of 12 landings over the prior model. I thought the increase in training would result in more landings.
  
  
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
