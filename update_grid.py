import re

with open('productos.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_grid = """                    <!-- Product 1: Escamizadores -->
                    <div class="relative group h-[450px] overflow-hidden bg-brand-dark cursor-pointer shadow-lg hover:shadow-2xl transition-all duration-500">
                        <img src="prod_escamizadores.jpg" alt="Escamizadores" class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-700 group-hover:scale-105 opacity-80 group-hover:opacity-100">
                        <div class="absolute inset-0 bg-gradient-to-t from-[#191817] via-[#191817]/40 to-transparent pointer-events-none"></div>
                        <div class="absolute bottom-0 left-0 p-8 w-full z-10 flex flex-col justify-end">
                            <div class="w-10 h-1 bg-brand-orange mb-4 transform origin-left group-hover:scale-x-150 transition-transform duration-500"></div>
                            <h3 class="text-white text-xl font-black uppercase tracking-tight leading-[1.2] group-hover:text-brand-orange transition-colors duration-500">
                                Escamizadores
                            </h3>
                        </div>
                    </div>

                    <!-- Product 2: Intercambiadores -->
                    <div class="relative group h-[450px] overflow-hidden bg-brand-dark cursor-pointer shadow-lg hover:shadow-2xl transition-all duration-500">
                        <img src="prod_intercambiadores.jpg" alt="Fabricación de intercambiadores de calor" class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-700 group-hover:scale-105 opacity-80 group-hover:opacity-100">
                        <div class="absolute inset-0 bg-gradient-to-t from-[#191817] via-[#191817]/60 to-transparent pointer-events-none"></div>
                        <div class="absolute bottom-0 left-0 p-8 w-full z-10 flex flex-col justify-end">
                            <div class="w-10 h-1 bg-brand-orange mb-4 transform origin-left group-hover:scale-x-150 transition-transform duration-500"></div>
                            <h3 class="text-white text-lg font-black uppercase tracking-tight leading-[1.3] group-hover:text-brand-orange transition-colors duration-500">
                                Fabricación de intercambiadores de calor y servicios de refluxado
                            </h3>
                        </div>
                    </div>

                    <!-- Product 3: Parrillas -->
                    <div class="relative group h-[450px] overflow-hidden bg-brand-dark cursor-pointer shadow-lg hover:shadow-2xl transition-all duration-500">
                        <img src="prod_parrillas.jpg" alt="Fabricación de Parrillas Viajeras" class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-700 group-hover:scale-105 opacity-80 group-hover:opacity-100">
                        <div class="absolute inset-0 bg-gradient-to-t from-[#191817] via-[#191817]/40 to-transparent pointer-events-none"></div>
                        <div class="absolute bottom-0 left-0 p-8 w-full z-10 flex flex-col justify-end">
                            <div class="w-10 h-1 bg-brand-orange mb-4 transform origin-left group-hover:scale-x-150 transition-transform duration-500"></div>
                            <h3 class="text-white text-xl font-black uppercase tracking-tight leading-[1.2] group-hover:text-brand-orange transition-colors duration-500">
                                Fabricación de Parrillas Viajeras
                            </h3>
                        </div>
                    </div>

                    <!-- Product 4: Reactores presion -->
                    <div class="relative group h-[450px] overflow-hidden bg-brand-dark cursor-pointer shadow-lg hover:shadow-2xl transition-all duration-500">
                        <img src="prod_reactores_presion.jpg" alt="Reactores sujetos a presión" class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-700 group-hover:scale-105 opacity-80 group-hover:opacity-100">
                        <div class="absolute inset-0 bg-gradient-to-t from-[#191817] via-[#191817]/50 to-transparent pointer-events-none"></div>
                        <div class="absolute bottom-0 left-0 p-8 w-full z-10 flex flex-col justify-end">
                            <div class="w-10 h-1 bg-brand-orange mb-4 transform origin-left group-hover:scale-x-150 transition-transform duration-500"></div>
                            <h3 class="text-white text-lg font-black uppercase tracking-tight leading-[1.2] group-hover:text-brand-orange transition-colors duration-500">
                                Fabricación de reactores sujetos a presión y temperatura
                            </h3>
                        </div>
                    </div>

                    <!-- Product 5: Rotores ventiladores -->
                    <div class="relative group h-[450px] overflow-hidden bg-brand-dark cursor-pointer shadow-lg hover:shadow-2xl transition-all duration-500">
                        <img src="prod_rotores.jpg" alt="Rotores para ventiladores" class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-700 group-hover:scale-105 opacity-80 group-hover:opacity-100">
                        <div class="absolute inset-0 bg-gradient-to-t from-[#191817] via-[#191817]/60 to-transparent pointer-events-none"></div>
                        <div class="absolute bottom-0 left-0 p-8 w-full z-10 flex flex-col justify-end">
                            <div class="w-10 h-1 bg-brand-orange mb-4 transform origin-left group-hover:scale-x-150 transition-transform duration-500"></div>
                            <h3 class="text-white text-[15px] font-black uppercase tracking-tight leading-[1.3] group-hover:text-brand-orange transition-colors duration-500">
                                Fabricación de rotores para ventiladores de tiro inducido, con recubrimiento anti-desgaste
                            </h3>
                        </div>
                    </div>

                    <!-- Product 6: Tachos -->
                    <div class="relative group h-[450px] overflow-hidden bg-brand-dark cursor-pointer shadow-lg hover:shadow-2xl transition-all duration-500">
                        <img src="prod_tachos.jpg" alt="Fabricación de tachos y calandrias" class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-700 group-hover:scale-105 opacity-80 group-hover:opacity-100">
                        <div class="absolute inset-0 bg-gradient-to-t from-[#191817] via-[#191817]/40 to-transparent pointer-events-none"></div>
                        <div class="absolute bottom-0 left-0 p-8 w-full z-10 flex flex-col justify-end">
                            <div class="w-10 h-1 bg-brand-orange mb-4 transform origin-left group-hover:scale-x-150 transition-transform duration-500"></div>
                            <h3 class="text-white text-xl font-black uppercase tracking-tight leading-[1.2] group-hover:text-brand-orange transition-colors duration-500">
                                Fabricación de tachos y calandrias
                            </h3>
                        </div>
                    </div>

                    <!-- Product 7: Reactores IAO -->
                    <div class="relative group h-[450px] overflow-hidden bg-brand-dark cursor-pointer shadow-lg hover:shadow-2xl transition-all duration-500">
                        <img src="prod_reactores_iao.jpg" alt="Reactores IAO" class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-700 group-hover:scale-105 opacity-80 group-hover:opacity-100">
                        <div class="absolute inset-0 bg-gradient-to-t from-[#191817] via-[#191817]/40 to-transparent pointer-events-none"></div>
                        <div class="absolute bottom-0 left-0 p-8 w-full z-10 flex flex-col justify-end">
                            <div class="w-10 h-1 bg-brand-orange mb-4 transform origin-left group-hover:scale-x-150 transition-transform duration-500"></div>
                            <h3 class="text-white text-xl font-black uppercase tracking-tight leading-[1.2] group-hover:text-brand-orange transition-colors duration-500">
                                Reactores IAO
                            </h3>
                        </div>
                    </div>

                    <!-- Product 8: Tanques Atmosfericos -->
                    <div class="relative group h-[450px] overflow-hidden bg-brand-dark cursor-pointer shadow-lg hover:shadow-2xl transition-all duration-500">
                        <img src="prod_tanques.jpg" alt="Tanques Atmosféricos IAO" class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-700 group-hover:scale-105 opacity-80 group-hover:opacity-100">
                        <div class="absolute inset-0 bg-gradient-to-t from-[#191817] via-[#191817]/40 to-transparent pointer-events-none"></div>
                        <div class="absolute bottom-0 left-0 p-8 w-full z-10 flex flex-col justify-end">
                            <div class="w-10 h-1 bg-brand-orange mb-4 transform origin-left group-hover:scale-x-150 transition-transform duration-500"></div>
                            <h3 class="text-white text-xl font-black uppercase tracking-tight leading-[1.2] group-hover:text-brand-orange transition-colors duration-500">
                                Tanques Atmosféricos IAO
                            </h3>
                        </div>
                    </div>

                    <!-- Product 9: Ventilador tiro forzado -->
                    <div class="relative group h-[450px] overflow-hidden bg-brand-dark cursor-pointer shadow-lg hover:shadow-2xl transition-all duration-500">
                        <img src="prod_ventilador_forzado.jpg" alt="Ventilador de tiro forzado IAO" class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-700 group-hover:scale-105 opacity-80 group-hover:opacity-100">
                        <div class="absolute inset-0 bg-gradient-to-t from-[#191817] via-[#191817]/40 to-transparent pointer-events-none"></div>
                        <div class="absolute bottom-0 left-0 p-8 w-full z-10 flex flex-col justify-end">
                            <div class="w-10 h-1 bg-brand-orange mb-4 transform origin-left group-hover:scale-x-150 transition-transform duration-500"></div>
                            <h3 class="text-white text-xl font-black uppercase tracking-tight leading-[1.2] group-hover:text-brand-orange transition-colors duration-500">
                                Ventilador de Tiro Forzado IAO
                            </h3>
                        </div>
                    </div>"""

# Find the grid string
start_str = '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">'
end_str = '</div>\n            </div>\n        </section>\n\n        <!-- CTA Final -->'

start_idx = content.find(start_str)
end_idx = content.find(end_str)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx + len(start_str)] + '\n' + new_grid + '\n                ' + content[end_idx:]
    with open('productos.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully replaced grid in productos.html")
else:
    print("Could not find start or end strings in productos.html")
