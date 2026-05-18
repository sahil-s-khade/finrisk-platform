import { Link } from "react-router-dom";

function LandingPage() {

  return (

    <div
      className="
        min-h-screen
        bg-gradient-to-br
        from-slate-950
        via-blue-950
        to-black
        text-white
      "
    >

      {/* NAVBAR */}

      <div
        className="
          flex
          items-center
          justify-between
          px-10
          py-6
        "
      >

        <div className="text-4xl font-extrabold">

          FinRisk AI

        </div>


        <div className="flex gap-6">

          <Link
            to="/dashboard"
            className="
              bg-blue-600
              hover:bg-blue-700
              px-6
              py-3
              rounded-xl
              font-semibold
              transition
            "
          >

            Open Dashboard

          </Link>

        </div>

      </div>



      {/* HERO SECTION */}

      <div
        className="
          max-w-7xl
          mx-auto
          px-10
          pt-24
          pb-20
        "
      >

        <div className="grid lg:grid-cols-2 gap-20 items-center">

          {/* LEFT */}

          <div>

            <div
              className="
                inline-block
                bg-blue-500/20
                text-blue-300
                px-5
                py-2
                rounded-full
                mb-8
                border
                border-blue-400/20
              "
            >

              AI-Powered Fraud Intelligence Platform

            </div>


            <h1
              className="
                text-6xl
                lg:text-7xl
                font-extrabold
                leading-tight
                mb-8
              "
            >

              Enterprise Fraud Detection
              Powered by AI

            </h1>


            <p
              className="
                text-gray-300
                text-xl
                leading-9
                mb-10
              "
            >

              FinRisk AI combines machine learning,
              anomaly detection,
              explainable AI,
              fraud analytics,
              and real-time monitoring
              to secure enterprise financial systems.

            </p>


            <div className="flex flex-wrap gap-5">

              <Link
                to="/dashboard"
                className="
                  bg-blue-600
                  hover:bg-blue-700
                  px-8
                  py-4
                  rounded-2xl
                  text-lg
                  font-bold
                  transition
                "
              >

                Launch Platform

              </Link>


              <Link
                to="/project-overview"
                className="
                  border
                  border-gray-500
                  hover:border-white
                  px-8
                  py-4
                  rounded-2xl
                  text-lg
                  font-bold
                  transition
                "
              >

                View Architecture

              </Link>

            </div>

          </div>



          {/* RIGHT */}

          <div
            className="
              bg-white/5
              border
              border-white/10
              backdrop-blur-lg
              rounded-[40px]
              p-10
              shadow-2xl
            "
          >

            <div className="grid grid-cols-2 gap-6">

              {/* CARD */}

              <div
                className="
                  bg-blue-500/10
                  border
                  border-blue-500/20
                  rounded-3xl
                  p-6
                "
              >

                <div className="text-5xl mb-4">

                  🤖

                </div>

                <div className="text-4xl font-bold mb-2">

                  98%

                </div>

                <div className="text-gray-300">

                  ML Accuracy

                </div>

              </div>



              {/* CARD */}

              <div
                className="
                  bg-red-500/10
                  border
                  border-red-500/20
                  rounded-3xl
                  p-6
                "
              >

                <div className="text-5xl mb-4">

                  🚨

                </div>

                <div className="text-4xl font-bold mb-2">

                  24/7

                </div>

                <div className="text-gray-300">

                  Live Monitoring

                </div>

              </div>



              {/* CARD */}

              <div
                className="
                  bg-green-500/10
                  border
                  border-green-500/20
                  rounded-3xl
                  p-6
                "
              >

                <div className="text-5xl mb-4">

                  ⚡

                </div>

                <div className="text-4xl font-bold mb-2">

                  REALTIME

                </div>

                <div className="text-gray-300">

                  Fraud Detection

                </div>

              </div>



              {/* CARD */}

              <div
                className="
                  bg-orange-500/10
                  border
                  border-orange-500/20
                  rounded-3xl
                  p-6
                "
              >

                <div className="text-5xl mb-4">

                  🧠

                </div>

                <div className="text-4xl font-bold mb-2">

                  XAI

                </div>

                <div className="text-gray-300">

                  Explainable AI

                </div>

              </div>

            </div>

          </div>

        </div>

      </div>



      {/* FEATURES */}

      <div
        className="
          max-w-7xl
          mx-auto
          px-10
          pb-24
        "
      >

        <h2
          className="
            text-5xl
            font-extrabold
            text-center
            mb-20
          "
        >

          Enterprise AI Features

        </h2>


        <div className="grid md:grid-cols-3 gap-8">

          {/* FEATURE */}

          <div
            className="
              bg-white/5
              border
              border-white/10
              rounded-3xl
              p-8
            "
          >

            <div className="text-5xl mb-6">

              📊

            </div>

            <h3 className="text-2xl font-bold mb-5">

              Fraud Analytics

            </h3>

            <p className="text-gray-300 leading-8">

              Enterprise-level fraud intelligence
              dashboards with predictive analytics
              and anomaly monitoring.

            </p>

          </div>



          {/* FEATURE */}

          <div
            className="
              bg-white/5
              border
              border-white/10
              rounded-3xl
              p-8
            "
          >

            <div className="text-5xl mb-6">

              🤖

            </div>

            <h3 className="text-2xl font-bold mb-5">

              Machine Learning

            </h3>

            <p className="text-gray-300 leading-8">

              Real-time fraud prediction systems
              powered by supervised ML models
              and AI scoring engines.

            </p>

          </div>



          {/* FEATURE */}

          <div
            className="
              bg-white/5
              border
              border-white/10
              rounded-3xl
              p-8
            "
          >

            <div className="text-5xl mb-6">

              🧠

            </div>

            <h3 className="text-2xl font-bold mb-5">

              Explainable AI

            </h3>

            <p className="text-gray-300 leading-8">

              Transparent AI decision systems
              providing fraud reasoning
              and enterprise explainability.

            </p>

          </div>

        </div>

      </div>

    </div>
  );
}

export default LandingPage;