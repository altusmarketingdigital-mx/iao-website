import re

with open('servicio-auditoria-cfd.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update title
content = re.sub(r'<title>.*?</title>', '<title>Reformas y Optimización | IAO</title>', content)
content = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="Servicio de optimización y repotenciación de calderas y equipos térmicos.">', content)

# Remove everything inside <main>
main_content_new = '''
    <main>
        <!-- Service Hero Section -->
        <section class="bg-[#191817] pt-28 pb-24 border-b-4 border-brand-orange relative overflow-hidden">
            <div class="absolute inset-0 opacity-[0.03] z-0" style="background-image: radial-gradient(circle at 100% 0%, #ffffff 0%, transparent 50%), radial-gradient(circle at 0% 100%, #FC5220 0%, transparent 50%);"></div>
            
            <div class="max-w-[1000px] mx-auto px-6 text-center relative z-10">
                <span class="text-brand-orange font-black uppercase tracking-[0.2em] text-sm mb-6 block">Soluciones de Ingeniería IAO</span>
                <h1 class="text-4xl md:text-6xl font-black text-white uppercase tracking-tighter mb-8 leading-[1.05]">
                    Reformas <span class="text-transparent bg-clip-text bg-gradient-to-r from-brand-orange to-orange-400">y Actualizaciones Térmicas</span>
                </h1>
                <p class="text-gray-400 text-lg md:text-xl font-medium max-w-3xl mx-auto leading-relaxed">
                    Modernización y repotenciación de equipos industriales para incrementar capacidad, eficiencia y confiabilidad operativa.
                </p>
            </div>
        </section>

        <!-- New Section Based on Image -->
        <section class="py-24 bg-white relative">
            <div class="max-w-[1080px] mx-auto px-6">
                <!-- Outer Container matching screenshot -->
                <div class="border border-gray-200 shadow-xl overflow-hidden bg-[#f8f9fa]">
                    
                    <!-- Header -->
                    <div class="bg-[#151821] py-5 px-8 flex justify-center">
                        <h2 class="text-2xl md:text-[2rem] font-black text-white tracking-tight uppercase leading-none">Optimización y Repotenciación de Caldera</h2>
                    </div>
                    
                    <!-- Content area -->
                    <div class="p-8 md:p-12 grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                        
                        <!-- Card Left -->
                        <div class="bg-white rounded-xl p-8 shadow-sm h-full flex flex-col justify-center">
                            <div class="mb-10">
                                <i class="fas fa-check-circle text-blue-500 text-[2.5rem] mb-4"></i>
                                <h3 class="text-2xl font-black text-gray-800 mb-1 tracking-tight">Caso de Éxito</h3>
                                <p class="text-gray-500 font-bold text-base">Caldera de Biomasa en Ingenio Azucarero</p>
                            </div>
                            
                            <div>
                                <div class="flex items-center gap-2 mb-4">
                                    <i class="fas fa-arrow-trend-up text-green-500 text-2xl"></i>
                                    <span class="text-green-600 font-black text-xl tracking-tight">Impacto Real</span>
                                </div>
                                <div class="flex items-baseline gap-3 mb-2">
                                    <span class="text-3xl font-black text-gray-900 tracking-tighter">11 TPH</span>
                                    <i class="fas fa-arrow-right text-gray-300 text-sm"></i>
                                    <span class="text-3xl font-black text-gray-900 tracking-tighter">35 TPH</span>
                                </div>
                                <p class="text-gray-500 font-bold text-sm">Incremento de capacidad</p>
                            </div>
                        </div>

                        <!-- Image Right -->
                        <div class="h-full flex items-center justify-center">
                            <img src="opt_step1.png" alt="Análisis CFD Optimización" class="w-full object-contain bg-black shadow-lg">
                        </div>

                    </div>
                </div>
            </div>
        </section>
    </main>
'''

# Replace <main>...</main>
content = re.sub(r'<main>.*?</main>', main_content_new, content, flags=re.DOTALL)

with open('reformas.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('reformas.html created.')
