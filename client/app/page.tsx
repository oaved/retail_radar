export default function Home() {
  return (
    <main
      className="relative min-h-screen flex flex-col items-center justify-center overflow-hidden"
      style={{
        background: "radial-gradient(ellipse at center, #c4b5fd 0%, #ede9fe 35%, #ffffff 70%)",
      }}
    >
      <div className="flex flex-col items-center text-center px-6">

        {/* Badge */}
        <div className="mb-6 inline-flex items-center gap-2 rounded-full border border-purple-200 bg-white/60 px-4 py-1.5 text-sm text-purple-600 backdrop-blur-sm">
          <span className="h-1.5 w-1.5 rounded-full bg-purple-500 animate-pulse" />
          AI-drivna insikter för detaljhandeln
        </div>

        {/* Heading */}
        <h1
          className="text-6xl sm:text-8xl font-bold tracking-tight mb-4 text-slate-900"
          style={{ letterSpacing: "-0.04em" }}
        >
          Retail
          <span
            className="text-transparent bg-clip-text"
            style={{ backgroundImage: "linear-gradient(135deg, #7c3aed, #a855f7)" }}
          >
            {" "}Radar
          </span>
        </h1>

        <p className="max-w-xl text-lg text-slate-500 mb-10 leading-relaxed">
          Hitta trender innan de kommer. Vår AI-drivna plattform analyserar miljontals signaler i realtid för att ge dig insikter som håller dig steget före i detaljhandeln.
        </p>

        {/* CTAs */}
        <div className="flex flex-col sm:flex-row gap-4">
          <button className="rounded-full bg-purple-600 text-white px-8 py-3 font-medium text-sm hover:bg-purple-700 cursor-pointer transition-all">
            Testa nu
          </button>
          <button className="rounded-full border border-purple-200 text-slate-600 px-8 py-3 font-medium text-sm bg-white/80 hover:bg-white/50 cursor-pointer transition-all">
            Se hur det fungerar
          </button>
        </div>
      </div>
    </main>
  );
}