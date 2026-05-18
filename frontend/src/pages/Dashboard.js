import { useEffect, useState } from "react";

import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";
import StatsCard from "../components/StatsCard";

import API from "../services/api";

import FraudPieChart from "../components/FraudPieChart";
import RiskBarChart from "../components/RiskBarChart";

function Dashboard() {

  const [dashboardData, setDashboardData] =
    useState(null);

  const [loading, setLoading] =
    useState(true);

  const [error, setError] =
    useState("");


  // JWT TOKEN
 const token = localStorage.getItem("token");


  useEffect(() => {

    const loadDashboard = async () => {

      try {

        const response = await API.get(

          "/dashboard/overview",

          {
            headers: {
              Authorization:
                `Bearer ${token}`
            }
          }
        );

        console.log(
          "Dashboard API:",
          response.data
        );

        setDashboardData(
          response.data
        );

      } catch (error) {

        console.error(
          "Dashboard Error:",
          error
        );

        setError(
          "Failed to load dashboard data"
        );

      } finally {

        setLoading(false);
      }
    };

    loadDashboard();

  }, [token]);


  // LOADING STATE
  if (loading) {

    return (

      <div className="p-10 text-3xl">

        Loading Dashboard...

      </div>
    );
  }


  // ERROR STATE
  if (error) {

    return (

      <div className="p-10 text-red-500 text-2xl">

        {error}

      </div>
    );
  }


  return (

    <div className="flex bg-gray-100 min-h-screen">

      <Sidebar />

      <div className="flex-1">

        <Navbar />

       <div className="p-6 lg:p-8 max-w-[1600px] mx-auto">

          {/* HERO SECTION */}

<div
  className="
    bg-gradient-to-r
    from-blue-900
    via-indigo-900
    to-black
    text-white
    p-10
    rounded-3xl
    shadow-2xl
    mb-10
  "
>

  <div className="
    flex
    flex-col
    md:flex-row
    md:items-center
    md:justify-between
    gap-8
  ">

    {/* LEFT */}

    <div>

      <h1 className="
        text-5xl
        font-extrabold
        mb-4
      ">

        FinRisk AI Platform

      </h1>

      <p className="
        text-xl
        text-gray-300
        leading-8
        max-w-3xl
      ">

        Enterprise-grade AI-powered fraud
        intelligence system for real-time
        financial risk detection, machine
        learning analytics, explainable AI,
        and live transaction monitoring.

      </p>

    </div>


    {/* RIGHT STATUS */}

    <div className="
      bg-white/10
      backdrop-blur-lg
      p-6
      rounded-2xl
      border
      border-white/20
      min-w-[280px]
    ">

      <div className="
        flex
        items-center
        justify-between
        mb-4
      ">

        <span className="text-gray-300">

          System Status

        </span>

        <span className="
          bg-green-500
          w-3
          h-3
          rounded-full
        ">

        </span>

      </div>


      <div className="space-y-3">

        <div className="
          flex
          justify-between
        ">

          <span className="text-gray-400">

            AI Engine

          </span>

          <span className="font-bold">

            ACTIVE

          </span>

        </div>


        <div className="
          flex
          justify-between
        ">

          <span className="text-gray-400">

            Fraud Detection

          </span>

          <span className="font-bold text-green-400">

            LIVE

          </span>

        </div>


        <div className="
          flex
          justify-between
        ">

          <span className="text-gray-400">

            ML Monitoring

          </span>

          <span className="font-bold text-blue-400">

            RUNNING

          </span>

        </div>

      </div>

    </div>

  </div>

</div>

{/* STATS SECTION */}

<div
  className="
    grid
    grid-cols-1
    lg:grid-cols-3
    gap-5
    mb-8
  "
>

  <StatsCard
    title="Total Transactions"
    value={
      dashboardData
      ?.transaction_metrics
      ?.total_transactions || 0
    }
    color="text-blue-600"
  />

  <StatsCard
    title="Fraud Transactions"
    value={
      dashboardData
      ?.transaction_metrics
      ?.fraud_transactions || 0
    }
    color="text-red-500"
  />

  <StatsCard
    title="High Risk Alerts"
    value={
      dashboardData
      ?.transaction_metrics
      ?.high_risk_transactions || 0
    }
    color="text-orange-500"
  />

</div>



{/* REAL-TIME ALERT SECTION */}

<div
  className="
    bg-white
    rounded-3xl
    shadow-lg
    p-6
    mb-10
    border
    border-gray-200
  "
>

  <div
    className="
      flex
      flex-col
      xl:flex-row
      xl:items-center
      xl:justify-between
      gap-8
    "
  >

    {/* LEFT CONTENT */}

    <div className="flex-1">

      <div
        className="
          flex
          items-center
          gap-3
          mb-4
        "
      >

        <div
          className="
            w-4
            h-4
            bg-red-500
            rounded-full
            animate-pulse
          "
        />

        <h2
          className="
            text-2xl
            font-bold
            text-red-600
          "
        >

          Real-Time Fraud Alerts

        </h2>

      </div>


      <p
        className="
          text-gray-600
          leading-7
          text-[17px]
          max-w-3xl
        "
      >

        FinRisk AI continuously monitors
        transaction pipelines, fraud scores,
        anomaly detection systems,
        and machine learning engines
        in real time across the platform.

      </p>

    </div>



    {/* ALERT BOXES */}

    <div
      className="
        grid
        grid-cols-2
        gap-4
        w-full
        xl:w-auto
      "
    >

      {/* BOX */}

      <div
        className="
          bg-red-50
          border
          border-red-100
          rounded-2xl
          px-5
          py-4
          text-center
          min-w-[150px]
          hover:shadow-lg
          transition
        "
      >

        <div className="text-2xl mb-1">
          🚨
        </div>

        <div
          className="
            text-2xl
            font-bold
            text-red-600
          "
        >
          12
        </div>

        <div
          className="
            text-sm
            text-red-500
            mt-1
          "
        >
          High Risk
        </div>

      </div>



      {/* BOX */}

      <div
        className="
          bg-orange-50
          border
          border-orange-100
          rounded-2xl
          px-5
          py-4
          text-center
          min-w-[150px]
          hover:shadow-lg
          transition
        "
      >

        <div className="text-2xl mb-1">
          ⚠️
        </div>

        <div
          className="
            text-2xl
            font-bold
            text-orange-600
          "
        >
          34
        </div>

        <div
          className="
            text-sm
            text-orange-500
            mt-1
          "
        >
          Medium Risk
        </div>

      </div>



      {/* BOX */}

      <div
        className="
          bg-blue-50
          border
          border-blue-100
          rounded-2xl
          px-5
          py-4
          text-center
          min-w-[150px]
          hover:shadow-lg
          transition
        "
      >

        <div className="text-2xl mb-1">
          🤖
        </div>

        <div
          className="
            text-xl
            font-bold
            text-blue-600
          "
        >
          ACTIVE
        </div>

        <div
          className="
            text-sm
            text-blue-500
            mt-1
          "
        >
          AI Engine
        </div>

      </div>



      {/* BOX */}

      <div
        className="
          bg-green-50
          border
          border-green-100
          rounded-2xl
          px-5
          py-4
          text-center
          min-w-[150px]
          hover:shadow-lg
          transition
        "
      >

        <div className="text-2xl mb-1">
          ✅
        </div>

        <div
          className="
            text-xl
            font-bold
            text-green-600
          "
        >
          LIVE
        </div>

        <div
          className="
            text-sm
            text-green-500
            mt-1
          "
        >
          Monitoring
        </div>

      </div>

    </div>

  </div>

</div>


          {/* OVERVIEW SECTION */}

          <div className="
            bg-white
            mt-10
            p-8
            rounded-2xl
            shadow-lg
          ">

            <h2 className="
              text-2xl
              font-bold
              mb-4
            ">

              Fraud Intelligence Overview

            </h2>

            <p className="
              text-gray-700
              leading-8
            ">

              FinRisk AI continuously monitors
              financial transactions using
              machine learning models,
              anomaly detection systems,
              explainable AI engines,
              and real-time fraud analytics.

            </p>

          </div>


          {/* CHARTS SECTION */}

          <div className="
            grid
            grid-cols-1
            md:grid-cols-2
            gap-6
            mt-10
          ">

            <FraudPieChart

              fraud={
                dashboardData
                ?.transaction_metrics
                ?.fraud_transactions || 0
              }

              normal={
                (
                  dashboardData
                  ?.transaction_metrics
                  ?.total_transactions || 0
                )

                -

                (

                  dashboardData
                  ?.transaction_metrics
                  ?.fraud_transactions || 0

                )
              }
            />


            <RiskBarChart />

          </div>


          {/* QUICK ACCESS PANEL */}

          <div className="
            bg-white
            mt-10
            p-8
            rounded-2xl
            shadow-lg
          ">

            <h2 className="
              text-2xl
              font-bold
              mb-4
            ">

              Platform Modules

            </h2>

            <div className="
              grid
              grid-cols-1
              md:grid-cols-2
              gap-4
            ">

              <div className="
                bg-gray-100
                p-5
                rounded-xl
              ">
                <h3 className="font-bold text-lg">
                  Fraud Analytics
                </h3>

                <p className="text-gray-600 mt-2">
                  ML fraud detection insights
                  and fraud pattern analysis.
                </p>
              </div>


              <div className="
                bg-gray-100
                p-5
                rounded-xl
              ">
                <h3 className="font-bold text-lg">
                  ML Monitoring
                </h3>

                <p className="text-gray-600 mt-2">
                  Monitor model performance
                  and fraud scoring pipelines.
                </p>
              </div>


              <div className="
                bg-gray-100
                p-5
                rounded-xl
              ">
                <h3 className="font-bold text-lg">
                  Explainable AI
                </h3>

                <p className="text-gray-600 mt-2">
                  Understand AI fraud decisions
                  with explainability engines.
                </p>
              </div>


              <div className="
                bg-gray-100
                p-5
                rounded-xl
              ">
                <h3 className="font-bold text-lg">
                  Live Monitoring
                </h3>

                <p className="text-gray-600 mt-2">
                  Real-time transaction monitoring
                  and fraud alert systems.
                </p>
              </div>

            </div>

          </div>

        </div>

      </div>

    </div>
  );
}

export default Dashboard;