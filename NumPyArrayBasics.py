import numpy as np
import matplotlib.pyplot as plt
import time 

plt.style.use('seaborn-v0_8-darkgrid')
np.random.seed(42)

print("Lab environment ready!")
print(f"NumPy version: {np.__version__}")

""""
#Part 1: Array Creation Playground
#1.1 Creating Your First Array
def exercise_1_1():
    #creating and visualizing arrays
    print("="*50)
    print("Exercise 1.1: Array Creation Methods")
    print("="*50)
    #1. an array of integers from 0-20
    array_range = np.arange(21)
    #2. an array of 50 evenly spaced points between 0 and 2pi
    array_linear = np.linspace(0, 2*np.pi, 50)
    #3. a 5x5 indentiy matrix
    identity_matrix = np.eye(5)
    #4. a 3x3 matrix filled w/ random integers 1-10
    random_matrix = np.random.randint(1, 11, (3, 3))
    
    #Visualization
    if array_range is not None and array_linear is not None:
        fig, axes = plt.subplots(2, 2, figsize=(10, 8))
        #Plot 1: Bar chart of range array
        axes[0,0].bar(range(len(array_range)), array_range, color='skyblue')
        axes[0,0].set_title('Array Range(0 to 20)')
        axes[0,0].set_xlabel('Index')
        axes[0,0].set_ylabel('Value')
        #Plot 2: Sine wave using linear space
        if array_linear is not None:
            sine_wave = np.sin(array_linear)
            axes[0,1].plot(array_linear, sine_wave, 'b-', linewidth=2)
            axes[0,1].set_title('Sine Wave')
            axes[0,1].set_xlabel('Radians')
            axes[0,1].set_ylabel('sin(x)')
            axes[0,1].grid(True)
        #Plot 3: Identity matrix as heatmap
        if identity_matrix is not None:
            im = axes[1,0].imshow(identity_matrix, cmap='RdBu', vmin=0, vmax=1)
            axes[1,0].set_title('5x5 Identity Matrix')
            plt.colorbar(im, ax=axes[1,0])
        #Plot 4: random matrix as heatmap
        if random_matrix is not None:
            im = axes[1,1].imshow(random_matrix, cmap='viridis')
            axes[1,1].set_title('3x3 Random Matrix')
            for i in range(3):
                for j in range(3):
                    axes[1,1].text(j, i, f'{random_matrix[i,j]}', ha='center', va='center', color='white')
            plt.colorbar(im, ax=axes[1,1])
        plt.tight_layout()
        plt.show()
    return array_range, array_linear, identity_matrix, random_matrix
arrays = exercise_1_1()
"""
"""
#1.2 Array Attributes Explorer
def exercise_1_2():
    #explore arrays attributes w/ different dimensional arrays
    print("\n" + "="*50)
    print("Exercise 1.2: Array Attributes")
    print("="*50)
    #Create Arrays of different dimensions
    arr_1d = np.array([1, 2, 3, 4, 5])
    arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
    arr_3d = np.array([[[1, 2], [3, 4], [5, 6], [7, 8]]])
    #Fill in the attributes for each array
    arrays = [
        ("1D Array", arr_1d),
        ("2D Array", arr_2d),
        ("3D Array", arr_3d)
    ]
    for name, arr in arrays:
        print(f"\n{name}:")
        print(f" Array:{arr}")
        
        #Shape
        rows = arr.shape[0]
        cols = arr.shape[1] if arr.ndim > 1 else 1
        print(f"Rows:{rows}, Columns:{cols}")
        #Size
        print(f"Size (total elements): {arr.size}")
        #Data Type of Elements (dtype)
        print(f"Data type: {arr.dtype}")
            #creating arrays w/ specific data types
        int_array = np.array([1, 2, 3], dtype=np.int32)
        float_array = np.array([1, 2, 3], dtype=np.float64)
        complex_array = np.array([1+2j, 3+4j], dtype=np.complex128)
        print(f"Int Array dtype: {int_array.dtype}")
        print(f"Float Array dtype: {float_array.dtype}")
        print(f"Complex Array dtype: {complex_array.dtype}")
        #Itemsize
        print(f"Item size: {arr.itemsize} bytes")
        #Total Bytes Consumed (nbytes)
        print(f"Total Bytes: {arr.nbytes}")
        
        #Create a Bar Chart comparing nbytes
        labels = [name for name, arr in arrays]
        nbytes = [arr.nbytes for _, arr in arrays]
        plt.figure(figsize=(6,4))
        plt.bar(labels, nbytes, color="skyblue", edgecolor="black")
        plt.title("Comparing nbyts between arrays")
        plt.xlabel("Array Type")
        plt.ylabel("Bytes")
        for i, val in enumerate(nbytes):
            plt.text(i, val + 5, str(val), ha='center', va='bottom', fontsize=10)
        plt.tight_layout()
        plt.show()
exercise_1_2()
"""
"""
#Part 2: Performance Comparison Challenge
#2.1 Numpy vs Python Lists
def exercise_2_1():
    #Create a visualization showing the speed difference
    print("\n" + "="*50)
    print("Exercise 2.1: The Great Performance Race!")
    print("="*50)
    #test different sizes
    sizes = [100, 1000, 10000, 100000]
    python_times = []
    numpy_times = []
    for size in sizes:
        #create data
        python_list = list(range(size))
        numpy_array = np.arange(size)
        #time python list operation
        start = time.time()
        python_result = [x * 2 for x in python_list]
        python_time = time.time() - start 
        python_times.append(python_time)
        #time numpy array operation
        start = time.time()
        numpy_result = numpy_array * 2
        numpy_time = time.time() - start
        numpy_times.append(numpy_time)
        #calculate speedup
        speedup = python_time / numpy_time if numpy_time > 0 else 0
        print(f"Size {size:6}: Python: {python_time:.4f}s, NumPy: {numpy_time:.4f}s, Speedup: {speedup:.1f}x")
    #create visualization
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (12, 5))
    #Plot 1: Time Comparison
    x = np.arange(len(sizes))
    width = 0.35
    ax1.bar(x - width/2, python_times, width, label = "Python List", color = "coral")
    ax1.bar(x + width/2, numpy_times, width, label = "NumPy Array", color = "skyblue")
    ax1.set_xlabel("Array Size")
    ax1.set_ylabel("Time (seconds)")
    ax1.set_title("Performance Comparison: Python vs NumPy")
    ax1.set_xticks(x)
    ax1.set_xticklabels(sizes)
    ax1.legend()
    ax1.set_yscale("log") #log scale for better visability
    #Plot 2: Speedup factor
    speedups = [p/n if n > 0 else 0 for p, n in zip(python_times, numpy_times)]
    ax2.plot(sizes, speedups, "go-", linewidth = 2, markersize = 10)
    ax2.set_xlabel("Array Size")
    ax2.set_ylabel("Speedup Factor")
    ax2.set_title("Numpy Speedup Over Python Lists")
    ax2.grid(True, alpha = 0.3)
    ax2.set_xscale("log")
    
    plt.tight_layout()
    plt.show()
    return python_times, numpy_times
exercise_2_1()
""" 

#Part 3: Fun with Array Operations
#3.1 Create Pixel Art with NumPy
from matplotlib.colors import ListedColormap
def exercise_3_1():
    #create pixel art using NumPy arrays and matplotlib
    print("\n" + "="*50)
    print("Exercise 3.1: NumPy Pixel Art")
    print("="*50)
    #create a smiley face // 0 for background, 1 for face, 2 for eyes/mouth
    smiley = np.zeros((10, 10))
    #face (yellow, circle)
    cx, cy = 4.5, 4.5
    r = 4
    for row in range(10):
        for col in range(10):
            if (col - cx) ** 2 + (row - cy) ** 2 <= r**2:
                smiley[row, col] = 1
    #eyes (black)
    smiley[3, 3] = 2
    smiley[3, 6] = 2
    #mouth
    smiley[6, 3:7] = 2
    smiley[5, 2] = 2
    smiley[5, 7] = 2
    cmap_smiley = ListedColormap(["white", "yellow", "black"])
    #display
    plt.figure(figsize=(6, 6))
    plt.imshow(smiley, cmap=cmap_smiley, interpolation="nearest")
    plt.title("Smiley")
    plt.axis("off")
    plt.show()
    return smiley
exercise_3_1()