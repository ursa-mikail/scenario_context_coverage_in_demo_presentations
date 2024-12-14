#!pip install anytree
import random
from anytree import Node, RenderTree
from anytree.exporter import DotExporter
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread

# Function to generate a node name
def generate_node_name(situation, scenario, scene, case, topic):
    return f"demo_situation{situation:02}_scenario{scenario:02}_scene{scene:02}_case_{case:02}_{topic}"

# Function to generate the tree
def generate_tree(max_situations, max_scenarios, max_scenes, max_cases, topic):
    root = Node("root")

    # Generate situations
    for situation in range(max_situations):
        situation_node = Node(generate_node_name(situation, 0, 0, 0, topic), parent=root)

        # Generate scenarios under each situation
        for scenario in range(random.randint(1, max_scenarios)):
            scenario_node = Node(generate_node_name(situation, scenario, 0, 0, topic), parent=situation_node)

            # Generate scenes under each scenario
            for scene in range(random.randint(1, max_scenes)):
                scene_node = Node(generate_node_name(situation, scenario, scene, 0, topic), parent=scenario_node)

                # Generate cases under each scene
                for case in range(random.randint(1, max_cases)):
                    Node(generate_node_name(situation, scenario, scene, case, topic), parent=scene_node)

    return root

# Function to print the tree
def print_tree(root):
    for pre, fill, node in RenderTree(root):
        print(f"{pre}{node.name}")

# Generate the tree
topic = "example_topic"
max_situations = 2 # 5
max_scenarios = 3
max_scenes = 2 # 4
max_cases = 3 # 2

root = generate_tree(max_situations, max_scenarios, max_scenes, max_cases, topic)

# Print the tree
print_tree(root)

# Export the tree to a .dot file for visualization
DotExporter(root).to_dotfile("tree.dot")

# Use Graphviz to render the .dot file to an image
from graphviz import Source

def render_dotfile(dotfile, output_format="png"):
    source = Source.from_file(dotfile)
    source.render(format=output_format)
    return source

# Render the .dot file to a PNG image
source = render_dotfile("tree.dot")

# Load and display the image using matplotlib
img = imread("tree.dot.png")
plt.figure(figsize=(5, 650))
plt.imshow(img)
plt.axis('off')
plt.show()

"""
root
├── demo_situation00_scenario00_scene00_case_00_example_topic
│   ├── demo_situation00_scenario00_scene00_case_00_example_topic
│   │   ├── demo_situation00_scenario00_scene00_case_00_example_topic
│   │   │   ├── demo_situation00_scenario00_scene00_case_00_example_topic
│   │   │   ├── demo_situation00_scenario00_scene00_case_01_example_topic
│   │   │   └── demo_situation00_scenario00_scene00_case_02_example_topic
│   │   └── demo_situation00_scenario00_scene01_case_00_example_topic
│   │       ├── demo_situation00_scenario00_scene01_case_00_example_topic
│   │       ├── demo_situation00_scenario00_scene01_case_01_example_topic
│   │       └── demo_situation00_scenario00_scene01_case_02_example_topic
│   └── demo_situation00_scenario01_scene00_case_00_example_topic
│       ├── demo_situation00_scenario01_scene00_case_00_example_topic
│       │   ├── demo_situation00_scenario01_scene00_case_00_example_topic
│       │   └── demo_situation00_scenario01_scene00_case_01_example_topic
│       └── demo_situation00_scenario01_scene01_case_00_example_topic
│           ├── demo_situation00_scenario01_scene01_case_00_example_topic
│           ├── demo_situation00_scenario01_scene01_case_01_example_topic
│           └── demo_situation00_scenario01_scene01_case_02_example_topic
└── demo_situation01_scenario00_scene00_case_00_example_topic
    └── demo_situation01_scenario00_scene00_case_00_example_topic
        ├── demo_situation01_scenario00_scene00_case_00_example_topic
        │   ├── demo_situation01_scenario00_scene00_case_00_example_topic
        │   ├── demo_situation01_scenario00_scene00_case_01_example_topic
        │   └── demo_situation01_scenario00_scene00_case_02_example_topic
        └── demo_situation01_scenario00_scene01_case_00_example_topic
            ├── demo_situation01_scenario00_scene01_case_00_example_topic
            ├── demo_situation01_scenario00_scene01_case_01_example_topic
            └── demo_situation01_scenario00_scene01_case_02_example_topic
"""