import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";

function ProjectOverview() {

  const technologies = [

    "React Frontend",
    "Flask REST APIs",
    "PostgreSQL Database",
    "JWT Authentication",
    "Fraud Detection ML Models",
    "Explainable AI Engine",
    "ETL Data Pipelines",
    "Real-Time Fraud Monitoring",
    "Machine Learning Analytics",
    "Risk Intelligence Engine"

  ];

  const modules = [

    {
      title: "Fraud Analytics",
      desc:
        "Real-time fraud scoring and transaction intelligence using AI-driven detection systems."
    },

    {
      title: "Live Monitoring",
      desc:
        "Continuous monitoring dashboard for suspicious transactions and fraud alerts."
    },

    {
      title: "Explainable AI",
      desc:
        "AI reasoning engine explaining why transactions are flagged as fraudulent."
    },

    {
      title: "ML Monitoring",
      desc:
        "Machine learning monitoring system tracking prediction performance and model accuracy."
    }

  ];

  return (

    <div className="flex bg-slate-100 min-h-screen">

      <Sidebar />

      <div className="flex-1">

        <Navbar />

        <div className="p-8">

          {/* HEADER */}

          <div
            className="
              bg-gradient-to-r
              from-indigo-700
              to-slate-900
              rounded-3xl
              p-10
              text-white
              shadow-2xl
              mb-10
            "
          >

            <h1 className="text-5xl font-bold mb-4">

              Project Overview

            </h1>

            <p className="text-lg text-gray-200 leading-8 max-w-4xl">

              FinRisk AI is a full-stack enterprise fraud
              intelligence platform built using React,
              Flask, PostgreSQL, Machine Learning,
              Explainable AI systems, and real-time
              monitoring pipelines.

            </p>

          </div>


          {/* ARCHITECTURE */}

          <div
            className="
              bg-white
              rounded-3xl
              shadow-lg
              p-8
              mb-10
            "
          >

            <h2 className="text-3xl font-bold mb-8">

              FinRisk AI Architecture

            </h2>

            <div
              className="
                grid
                grid-cols-1
                md:grid-cols-2
                lg:grid-cols-3
                gap-6
              "
            >

              {
                technologies.map((tech, index) => (

                  <div

                    key={index}

                    className="
                      bg-slate-50
                      border
                      border-slate-200
                      rounded-2xl
                      p-5
                      hover:shadow-lg
                      transition
                    "
                  >

                    <div className="flex items-center gap-3">

                      <div
                        className="
                          w-3
                          h-3
                          bg-indigo-600
                          rounded-full
                        "
                      />

                      <h3 className="font-semibold text-lg">

                        {tech}

                      </h3>

                    </div>

                  </div>
                ))
              }

            </div>

          </div>


          {/* CORE MODULES */}

          <div
            className="
              bg-white
              rounded-3xl
              shadow-lg
              p-8
            "
          >

            <h2 className="text-3xl font-bold mb-8">

              Core Platform Modules

            </h2>

            <div
              className="
                grid
                grid-cols-1
                md:grid-cols-2
                gap-8
              "
            >

              {
                modules.map((module, index) => (

                  <div

                    key={index}

                    className="
                      bg-gradient-to-br
                      from-slate-50
                      to-slate-100
                      rounded-2xl
                      p-6
                      border
                      border-slate-200
                      hover:shadow-xl
                      transition
                    "
                  >

                    <h3
                      className="
                        text-2xl
                        font-bold
                        mb-4
                        text-indigo-700
                      "
                    >

                      {module.title}

                    </h3>

                    <p
                      className="
                        text-gray-700
                        leading-8
                      "
                    >

                      {module.desc}

                    </p>

                  </div>
                ))
              }

            </div>

          </div>

        </div>

      </div>

    </div>
  );
}

export default ProjectOverview;