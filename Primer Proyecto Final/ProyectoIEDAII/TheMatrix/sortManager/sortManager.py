class SortManager():
	listaOrdenada = []
	def dataToSort(self,data):
		self.listaOrdenada = []
		self.oneSort(data,data[0].keys())
		return self.listaOrdenada
	def oneSort(self,data,element):                       
	    if len(data) == 1:                              
	        self.listaOrdenada.append(data[0])               
	        return                                      
	    else:
	        low = []                                    
	        high = []                                   
	        i = 0                                       
	        while i < len(data):                                               
	            if data[i].keys() < element:                   
	                low.append(data[i])                 
	            else:
	                high.append(data[i])                
	            i += 1                                  
	        if not low:                           
	            if high == data:                        
	                e = high[len(high)-1]               
	                if high[0] != e:                    
	                    high[0],high[len(high)-1] = high[len(high)-1], high[0] 
	                    self.oneSort(high, e.keys())             
	                else:
	                    x = 0                           
	                    while x < len(high):            
	                        if data[x] != e:            
	                            e = data[x]             
	                            break                   
	                        x += 1                      
	                    if e != high[len(high)-1]:      
	                        self.oneSort(high, e.keys())         
	                    else:
	                        listaOrdenada += high       
	            else:
	                self.oneSort(high, high[len(high)-1].keys()) 
	            return
	        else:
	            self.oneSort(low, low[0].keys())                 
	            self.oneSort(high, high[len(high)-1].keys())     
	    return self.listaOrdenada                            