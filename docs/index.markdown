---
layout: home
---

<link rel="stylesheet" href="css/bootstrap-carousel.css">

<style>
    .text-content {
        overflow: hidden;
        margin-top: 10px;
        text-align: justify;
    }

    .logo {
        width: 250px;
        float: right;
        margin-left: 20px;
        margin-bottom: 10px;
    }

    .research-line-header {
        cursor: pointer;
        padding: 10px;
        background-color: #f0f0f0;
        border: 1px solid #ccc;
        margin-top: 5px;
    }

    .research-line-header:hover {
        background-color: #e9e9e9;
    }

    .research-content {
        padding: 10px;
        border: 1px solid #ddd;
        border-top: none;
    }

    #research-lines-nav button {
        margin: 0 10px;
        color: #333;
        background-color: #fff;
        border: 1px solid #ddd;
    }

    #research-lines-nav button.active {
        color: #fff;
        background-color: #007bff;
        border-color: #007bff;
    }

    .research-content {
        padding: 20px;
        border: 1px solid #ddd;
        margin-top: 10px;
        display: none; /* Initially hide all */
    }

    .research-content.active {
        display: block; /* Show active content */
    }

    .card {
        margin-top: 20px;
        display: flex;
        align-items: center;
    }

    .card img {
        height: 150px;
        width: 150px;
        object-fit: cover;
        margin-right: 20px;
    }

    .card-body {
        padding: 0;
    }

    .card-title {
        margin-bottom: 15px;
    }
</style>

<div class="text-content">
    <img src="images/NAIRlogo.png" class="logo" alt="Neuroinspired AI">
    <p><strong>The <em>Neuroscience-inspired Artificial Intelligence and Robotics (NAIR)</em> research group belongs to the <a href="https://www.csic.es/en/csic">Spanish National Research Council (CSIC)</a>, <a href="https://www.cinc.csic.es/">Cajal International Neuroscience Center (CINC)</a>.</strong> Our research <em>transforms our understanding of the brain into future technologies</em>. It aims to improve artificial intelligence and robotic systems by studying how humans perceive and interact with their bodies, while also uncovering the internal mechanisms of information processing in the brain. We develop novel algorithms for learning, estimation, and control of complex systems based on findings from neuroscience, and evaluate them on robotic platforms (humanoids, manipulators, exoskeletons). Our models are not only relevant to disciplines, such as computational neuroscience, robotics, and cognitive science, but also have practical applications in human-centered solutions such as healthcare, human-robot interaction, wearable robotics, and more. Our goal is to achieve human-like embodied intelligence in robots, <ins>enabling them to act and adapt to complex real-world interactions, which is one of the key challenges of this century</ins>.</p>

    <p><strong>Experience:</strong> Our research group has over ten years of experience in brain-inspired machine learning models for robot perception and action. We have been pioneers in successfully deploying neuroscience-inspired models (e.g., predictive coding) on humanoid robots, as well as replicating experiments of human perception on robotic systems (e.g., rubber hand illusion). We are internationally recognized for our active inference approach to robotics, which is a framework inspired by neuroscience that describes the brain as a Bayesian approximate inference machine. Currently, we are investigating new theoretical applied probabilistic models in the following topics:</p>
</div>

<div class="container">
    <h2 class="text-center">Research Lines</h2>
    <div class="row">
        <div class="col-md-6">
            <div class="card">
                <img src="images/research-lines/R1-neuroAI.gif" class="card-img-left" alt="Neuroinspired AI">
                <div class="card-body">
                    <h5 class="card-title"><b>Neuroscience-inspired Artificial Intelligence</b></h5>
                    <p class="card-text">Developing AI systems inspired by the complexity and efficiency of the human brain to create adaptive and efficient algorithms for areas, such as healthcare, robotics, and industry</p>
                </div>
            </div>
        </div>
        <div class="col-md-6">
            <div class="card">
                <img src="images/research-lines/R2-robotlearning.png" class="card-img-left" alt="Robotic Learning">
                <div class="card-body">
                    <h5 class="card-title"><b>Robot Learning</b></h5>
                    <p class="card-text">Reinforcement Learning for Wearable Robotics. Integration of machine learning with robotics to develop personalized assistive devices, enhancing the quality of life for individuals with disabilities through improved mobility and independence.</p>
                </div>
            </div>
        </div>
        <div class="col-md-6">
            <div class="card">
                <img src="images/research-lines/R3-spikingcontrol.png" class="card-img-left" alt="Spiking Control">
                <div class="card-body">
                    <h5 class="card-title"><b>Spiking Control</b></h5>
                    <p class="card-text">Exploring the potential of spiking neural networks (SNNs) to create low-power-low-latency estimation and control algorithms for applications like autonomous vehicles, wearables, and neurotechnology</p>
                </div>
            </div>
        </div>
        <div class="col-md-6">
            <div class="card">
                <img src="images/research-lines/R4-bodyperception.png" class="card-img-left" alt="Computational Models of Body Perception">
                <div class="card-body">
                    <h5 class="card-title"><b>Computational Models of Body Perception</b></h5>
                    <p class="card-text">Replicating and understanding human body perception through computational models, with applications in virtual reality, robotics, and healthcare.</p>
                </div>
            </div>
        </div>
        <div class="col-md-6">
            <div class="card">
                <img src="images/research-lines/R5-awareness.png" class="card-img-left" alt="Self-Perception and Synthetic Consciousness">
                <div class="card-body">
                    <h5 class="card-title"><b>Self-Perception and Synthetic Consciousness</b></h5>
                    <p class="card-text">Exploring artificial consciousness and self-awareness in machines to create intelligent systems that understand human emotions and intentions, bridging the gap between artificial and biological intelligence.</p>
                </div>
            </div>
        </div>
    </div>
</div>

<br />

<div class="container">
    <h2 class="text-center">Group randomly selected pics</h2>
<div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel" style="margin-bottom: 20px;">
    <ol class="carousel-indicators">
        <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
    </ol>
    <div class="carousel-inner">
        <div class="carousel-item active">
            <img src="/images/home-slider/f.elconfidencial.com_original_42e_f46_45a_42ef4645abb3c89a61db4fd111641a44.jpg" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
            <img src="/images/home-slider/Robots-inventores-imitaran-la-forma-de-crear-herramientas-de-los-humanos-primitivos.jpg" class="d-block w-100" alt="...">
        </div>
    </div>
    <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
    </a>
    <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
    </a>
</div>
</div>

<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>


