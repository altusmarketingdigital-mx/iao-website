import re

with open('reformas.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_main = '''
    <main>
        <!-- Hero Section -->
        <section class="bg-[#191817] pt-28 pb-24 border-b-4 border-brand-orange relative overflow-hidden">
            <div class="absolute inset-0 opacity-[0.03] z-0" style="background-image: radial-gradient(circle at 100% 0%, #ffffff 0%, transparent 50%), radial-gradient(circle at 0% 100%, #FC5220 0%, transparent 50%);"></div>
            
            <div class="max-w-[1000px] mx-auto px-6 text-center relative z-10">
                <span class="text-brand-orange font-black uppercase tracking-[0.2em] text-sm mb-6 block">Caso de Éxito IAO</span>
                <h1 class="text-4xl md:text-6xl font-black text-white uppercase tracking-tighter mb-6 leading-[1.05]">
                    Optimización y Repotenciación <span class="text-transparent bg-clip-text bg-gradient-to-r from-brand-orange to-orange-400">de Caldera</span>
                </h1>
                <p class="text-gray-400 text-lg md:text-xl font-medium max-w-3xl mx-auto leading-relaxed">
                    Transformación integral de caldera de biomasa en ingenio azucarero. Triplicamos la capacidad sin necesidad de reemplazo.
                </p>
            </div>
        </section>

        <!-- Problemas y Solución -->
        <section class="py-24 bg-white relative">
            <div class="max-w-[1280px] mx-auto px-6">
                
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-start">
                    
                    <!-- Problemas Identificados -->
                    <div>
                        <div class="flex items-center gap-3 mb-6">
                            <span class="w-10 h-1 bg-red-500"></span>
                            <span class="text-brand-dark font-black uppercase text-xs tracking-widest text-red-500">Antes de la Intervención</span>
                        </div>
                        <h2 class="text-3xl font-black leading-[1.1] text-brand-dark uppercase tracking-tight mb-8">
                            Problemas Identificados
                        </h2>
                        
                        <div class="space-y-6">
                            <div class="flex gap-4 items-start">
                                <div class="w-10 h-10 rounded-full bg-red-50 text-red-500 flex items-center justify-center flex-shrink-0 mt-1">
                                    <i class="fas fa-exclamation-triangle"></i>
                                </div>
                                <div>
                                    <h4 class="text-lg font-bold text-gray-900 mb-1">Ineficiencias Críticas</h4>
                                    <p class="text-gray-600 font-medium">Baja capacidad real de generación y un consumo de bagazo excesivamente alto.</p>
                                </div>
                            </div>
                            <div class="flex gap-4 items-start">
                                <div class="w-10 h-10 rounded-full bg-red-50 text-red-500 flex items-center justify-center flex-shrink-0 mt-1">
                                    <i class="fas fa-wind"></i>
                                </div>
                                <div>
                                    <h4 class="text-lg font-bold text-gray-900 mb-1">Mala Distribución de Gases</h4>
                                    <p class="text-gray-600 font-medium">Flujos inestables y canales preferenciales dentro del sistema térmico.</p>
                                </div>
                            </div>
                            <div class="flex gap-4 items-start">
                                <div class="w-10 h-10 rounded-full bg-red-50 text-red-500 flex items-center justify-center flex-shrink-0 mt-1">
                                    <i class="fas fa-cogs"></i>
                                </div>
                                <div>
                                    <h4 class="text-lg font-bold text-gray-900 mb-1">Desgaste Prematuro</h4>
                                    <p class="text-gray-600 font-medium">Falla y deterioro de componentes mecánicos por sobreesfuerzo térmico.</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- CFD Image -->
                    <div class="relative bg-gray-50 rounded-2xl p-4 border border-gray-100 shadow-xl group">
                        <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent z-10 rounded-2xl flex flex-col justify-end p-8">
                            <span class="text-brand-orange font-bold text-sm tracking-widest uppercase mb-2">Simulación de fluidos</span>
                            <h3 class="text-white text-xl font-black uppercase">Análisis CFD para diagnóstico</h3>
                        </div>
                        <img src="opt_step1.png" alt="Simulación CFD IAO" class="w-full h-auto rounded-xl object-cover mix-blend-multiply group-hover:scale-[1.02] transition-transform duration-500">
                    </div>
                </div>

            </div>
        </section>

        <!-- Solución Implementada Grid -->
        <section class="py-24 bg-[#191817] text-white">
            <div class="max-w-[1280px] mx-auto px-6">
                
                <div class="mb-16">
                    <span class="text-brand-orange font-black uppercase tracking-widest text-sm mb-4 block">Estrategia Integral</span>
                    <h2 class="text-4xl font-black uppercase tracking-tight leading-none">
                        Solución Implementada
                    </h2>
                    <p class="text-gray-400 font-medium mt-6 max-w-2xl text-lg">
                        Uso de tecnología avanzada y rediseño interno profundo para estabilizar la unidad.
                    </p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                    <!-- Ingeniería -->
                    <div class="bg-[#232220] p-8 border-t-4 border-brand-orange hover:-translate-y-2 transition-transform duration-300">
                        <i class="fas fa-laptop-code text-4xl text-brand-orange mb-6 block"></i>
                        <h3 class="text-xl font-bold uppercase tracking-tight mb-4">Ingeniería de Detalle</h3>
                        <p class="text-gray-400 text-sm leading-relaxed">
                            Uso de simulación CFD (Dinámica de Fluidos Computacional) de alta precisión para evaluar velocidad, temperatura y presión, identificando así los puntos exactos de ineficiencia.
                        </p>
                    </div>

                    <!-- Rediseño -->
                    <div class="bg-[#232220] p-8 border-t-4 border-blue-500 hover:-translate-y-2 transition-transform duration-300">
                        <i class="fas fa-project-diagram text-4xl text-blue-500 mb-6 block"></i>
                        <h3 class="text-xl font-bold uppercase tracking-tight mb-4">Rediseño de Flujo</h3>
                        <ul class="space-y-3 text-sm text-gray-400">
                            <li><strong class="text-white">Mamparas internas:</strong> Diseñadas para controlar y distribuir el flujo de gases.</li>
                            <li><strong class="text-white">Placa perforada:</strong> Uniformiza el paso de gases eliminando canales preferenciales.</li>
                            <li><strong class="text-white">Redirección:</strong> Optimización de la trayectoria térmica hacia el haz de tubos.</li>
                        </ul>
                    </div>

                    <!-- Equipos -->
                    <div class="bg-[#232220] p-8 border-t-4 border-green-500 hover:-translate-y-2 transition-transform duration-300">
                        <i class="fas fa-fan text-4xl text-green-500 mb-6 block"></i>
                        <h3 class="text-xl font-bold uppercase tracking-tight mb-4">Actualización de Equipos</h3>
                        <p class="text-gray-400 text-sm leading-relaxed">
                            Reemplazo estratégico de ventiladores de sobrefuego y de tiro inducido por nuevos equipos de mayor eficiencia aerodinámica y capacidad de respuesta.
                        </p>
                    </div>
                </div>

            </div>
        </section>

        <!-- Etapas del Proyecto -->
        <section class="py-24 bg-gray-50 border-b border-gray-200">
            <div class="max-w-[1280px] mx-auto px-6">
                
                <div class="text-center mb-16">
                    <h2 class="text-3xl font-black uppercase tracking-tight text-brand-dark mb-4">Etapas y Ejecución</h2>
                    <div class="inline-flex items-center gap-3 bg-brand-orange/10 px-6 py-3 rounded-full text-brand-orange font-bold">
                        <i class="far fa-clock text-xl"></i>
                        <span>Duración total: 78 días</span>
                    </div>
                </div>

                <!-- Timeline -->
                <div class="grid grid-cols-1 md:grid-cols-4 gap-6 relative">
                    <!-- Progress Line background (desktop) -->
                    <div class="hidden md:block absolute top-[40px] left-0 w-full h-1 bg-gray-200 z-0"></div>

                    <!-- Step 1 -->
                    <div class="relative z-10 flex flex-col items-center md:items-start text-center md:text-left">
                        <div class="w-20 h-20 bg-white rounded-full border-4 border-brand-orange shadow-md flex items-center justify-center mb-6 text-brand-orange text-2xl">
                            <i class="fas fa-drafting-compass"></i>
                        </div>
                        <h4 class="text-lg font-black uppercase text-brand-dark mb-2">Ingeniería</h4>
                        <p class="text-gray-500 text-sm">Diseño detallado y validación técnica mediante herramientas digitales avanzadas.</p>
                    </div>

                    <!-- Step 2 -->
                    <div class="relative z-10 flex flex-col items-center md:items-start text-center md:text-left">
                        <div class="w-20 h-20 bg-white rounded-full border-4 border-brand-orange shadow-md flex items-center justify-center mb-6 text-brand-orange text-2xl">
                            <i class="fas fa-hammer"></i>
                        </div>
                        <h4 class="text-lg font-black uppercase text-brand-dark mb-2">Desmantelamiento</h4>
                        <p class="text-gray-500 text-sm">Remoción de equipos obsoletos de forma segura y estructurada.</p>
                    </div>

                    <!-- Step 3 -->
                    <div class="relative z-10 flex flex-col items-center md:items-start text-center md:text-left">
                        <div class="w-20 h-20 bg-white rounded-full border-4 border-brand-orange shadow-md flex items-center justify-center mb-6 text-brand-orange text-2xl">
                            <i class="fas fa-industry"></i>
                        </div>
                        <h4 class="text-lg font-black uppercase text-brand-dark mb-2">Fabricación</h4>
                        <p class="text-gray-500 text-sm">Construcción propia de componentes bajo altos estándares de calidad.</p>
                    </div>

                    <!-- Step 4 -->
                    <div class="relative z-10 flex flex-col items-center md:items-start text-center md:text-left">
                        <div class="w-20 h-20 bg-brand-orange rounded-full border-4 border-brand-orange shadow-md flex items-center justify-center mb-6 text-white text-2xl">
                            <i class="fas fa-check-double"></i>
                        </div>
                        <h4 class="text-lg font-black uppercase text-brand-dark mb-2">Instalación</h4>
                        <p class="text-gray-500 text-sm">Montaje en campo, supervisión y puesta en marcha con equipo especializado.</p>
                    </div>

                </div>

            </div>
        </section>

        <!-- Impacto Real (Results Card) -->
        <section class="py-24 bg-white relative overflow-hidden">
            <!-- Background element -->
            <div class="absolute right-[-10%] top-[-20%] w-[50%] h-[140%] bg-gray-50 -rotate-12 z-0"></div>

            <div class="max-w-[1080px] mx-auto px-6 relative z-10">
                <div class="border border-gray-200 shadow-2xl rounded-2xl overflow-hidden bg-white">
                    
                    <div class="bg-gradient-to-r from-[#151821] to-[#1e2230] py-6 px-10 flex justify-between items-center border-b-4 border-green-500">
                        <h2 class="text-3xl font-black text-white tracking-tight uppercase">Impacto Real y Resultados</h2>
                        <i class="fas fa-award text-4xl text-green-400 opacity-80"></i>
                    </div>
                    
                    <div class="p-10 md:p-14">
                        <p class="text-xl text-gray-700 font-medium mb-12 text-center max-w-3xl mx-auto">
                            El proyecto logró triplicar la capacidad de la caldera <strong class="text-brand-dark">sin necesidad de reemplazarla por una nueva.</strong>
                        </p>
                        
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12">
                            <!-- Inicial -->
                            <div class="bg-gray-50 rounded-xl p-8 text-center border border-gray-100 flex flex-col justify-center">
                                <span class="text-gray-500 font-bold uppercase tracking-widest text-xs mb-3 block">Capacidad Inicial</span>
                                <div class="text-4xl font-black text-gray-800">11 <span class="text-xl text-gray-500">TPH</span></div>
                            </div>
                            
                            <!-- Arrow -->
                            <div class="hidden md:flex items-center justify-center">
                                <div class="w-16 h-16 rounded-full bg-green-50 text-green-500 flex items-center justify-center shadow-inner">
                                    <i class="fas fa-arrow-right text-2xl"></i>
                                </div>
                            </div>

                            <!-- Final -->
                            <div class="bg-green-50 rounded-xl p-8 text-center border border-green-100 shadow-md transform scale-105">
                                <span class="text-green-600 font-bold uppercase tracking-widest text-xs mb-3 block">Capacidad Final</span>
                                <div class="text-5xl font-black text-green-600">35 <span class="text-2xl text-green-500/70">TPH</span></div>
                            </div>
                        </div>

                        <!-- Incremento & Beneficios -->
                        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center bg-gray-50 rounded-xl p-8 border border-gray-100">
                            <div class="text-center lg:text-left border-b lg:border-b-0 lg:border-r border-gray-200 pb-8 lg:pb-0 lg:pr-8">
                                <span class="text-green-500 text-6xl block mb-2"><i class="fas fa-arrow-trend-up"></i></span>
                                <div class="text-5xl font-black text-brand-dark tracking-tighter mb-2">+218%</div>
                                <p class="text-gray-500 font-bold uppercase tracking-widest text-sm">Incremento en generación</p>
                            </div>
                            
                            <div>
                                <h4 class="text-lg font-black uppercase text-brand-dark mb-4">Beneficios Adicionales:</h4>
                                <ul class="space-y-3">
                                    <li class="flex items-center gap-3 text-gray-600 font-medium"><i class="fas fa-check-circle text-brand-orange"></i> Mayor eficiencia térmica.</li>
                                    <li class="flex items-center gap-3 text-gray-600 font-medium"><i class="fas fa-check-circle text-brand-orange"></i> Menor consumo de bagazo.</li>
                                    <li class="flex items-center gap-3 text-gray-600 font-medium"><i class="fas fa-check-circle text-brand-orange"></i> Mayor confiabilidad y vida útil.</li>
                                    <li class="flex items-center gap-3 text-gray-600 font-medium"><i class="fas fa-check-circle text-brand-orange"></i> Solución altamente sostenible.</li>
                                </ul>
                            </div>
                        </div>

                    </div>
                </div>
            </div>
        </section>

        <!-- CTA Section -->
        <section class="bg-brand-orange py-20 relative overflow-hidden">
            <div class="absolute inset-0 opacity-10 bg-[url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMCIgaGVpZ2h0PSIyMCI+CgkJPGNpcmNsZSBjeD0iMiIgY3k9IjIiIHI9IjIiIGZpbGw9IiNmZmYiLz4KCTwvc3ZnPg==')]"></div>
            <div class="max-w-[1000px] mx-auto px-6 text-center relative z-10">
                <h2 class="text-3xl md:text-5xl font-black text-black uppercase tracking-tighter mb-6">¿Necesitas un diagnóstico?</h2>
                <p class="text-black/80 text-xl font-medium mb-10 max-w-2xl mx-auto">
                    Obtén un diagnóstico profesional de calderas con los especialistas de IAO y descubre el verdadero potencial de tu planta.
                </p>
                <a href="https://wa.me/523323488430" target="_blank" class="inline-flex items-center gap-4 bg-brand-dark text-white hover:bg-white hover:text-brand-dark transition-colors duration-300 px-8 py-5 rounded-full font-black uppercase tracking-widest text-sm shadow-xl group">
                    <i class="fab fa-whatsapp text-2xl text-green-400 group-hover:text-green-500"></i> +52 33 2348 8430
                </a>
            </div>
        </section>

    </main>
'''

content = re.sub(r'<main>.*?</main>', new_main, content, flags=re.DOTALL)

with open('reformas.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('reformas.html content updated.')
