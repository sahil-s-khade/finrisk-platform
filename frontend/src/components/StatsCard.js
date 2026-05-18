function StatsCard({

  title,
  value,
  color

}) {

  return (

    <div
      className="
        bg-white
        rounded-3xl
        p-8
        shadow-lg
        hover:shadow-2xl
        transition-all
        duration-300
        hover:-translate-y-2
        border
        border-gray-100
        relative
        overflow-hidden
      "
    >

      {/* TOP GLOW */}

      <div
        className={`
          absolute
          top-0
          left-0
          w-full
          h-2
          ${color.replace("text", "bg")}
        `}
      />



      {/* TITLE */}

      <div className="
        text-gray-500
        text-lg
        font-medium
        mb-4
      ">

        {title}

      </div>



      {/* VALUE */}

      <div
        className={`
          text-6xl
          font-extrabold
          ${color}
        `}
      >

        {value}

      </div>



      {/* TREND */}

      <div className="
        mt-6
        flex
        items-center
        justify-between
      ">

        <div className="
          text-sm
          text-gray-400
        ">

          Real-time analytics

        </div>


        <div className="
          bg-green-100
          text-green-600
          px-3
          py-1
          rounded-full
          text-sm
          font-bold
        ">

          +12%

        </div>

      </div>

    </div>
  );
}

export default StatsCard;